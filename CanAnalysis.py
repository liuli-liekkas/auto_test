import ctypes
from ctypes import wintypes
import numpy as np
from cantools import database


class Struct_INIT_CONFIG(ctypes.Structure):
	_fields_ = (("AccCode", wintypes.DWORD),
				("AccMask", wintypes.DWORD),
				("Reserved", wintypes.DWORD),
				("Filter", ctypes.c_ubyte),
				("Timing0", ctypes.c_ubyte),
				("Timing1", ctypes.c_ubyte),
				("Mode", ctypes.c_ubyte))


class Struct_CAN_OBJ(ctypes.Structure):
	_fields_ = [("ID", ctypes.c_uint),
				("TimeStamp", ctypes.c_uint),
				("TimeFlag", ctypes.c_ubyte),
				("SendType", ctypes.c_ubyte),
				("RemoteFlag", ctypes.c_ubyte),
				("ExternFlag", ctypes.c_ubyte),
				("DataLen", ctypes.c_ubyte),
				("Data", ctypes.c_ubyte * 8),
				("Reserved", ctypes.c_ubyte * 3)]


class CanControl:
	def __init__(self):
		self.db = database.load_file('./dbc/ARS408_can_database.dbc')
		self.canDLL = ctypes.CDLL('D:\\files\python_learn\\auto_test\\dll\\ECanVci64.dll')
		# self.canDLL = ctypes.CDLL('./dll/ECanVci64.dll')
		self.struct_initconfig = Struct_INIT_CONFIG(0, 0xFFFFFFFF, 0, 0, 0, 0x1C, 0)
		self.Struct_USBCAN2C = 4
		self.STATUS_OK = 1
		self.data = np.array([[-1, -1, -1, -1, -1, -1, -1]])
		# 定义DBC数据格式
		self.id_start = 0
		self.id_length = 8
		self.id_factor = 1
		self.id_offset = 0
		self.id_start_handle = (self.id_start // 8 + 1) * 8 - self.id_start % 8 - self.id_length
		self.dist_long_start = 19
		self.dist_long_length = 13
		self.dist_long_factor = 0.2
		self.dist_long_offset = -500
		self.dist_long_start_handle = (self.dist_long_start // 8 + 1) * 8 - self.dist_long_start % 8 - self.dist_long_length
		self.dist_lat_start = 24
		self.dist_lat_length = 11
		self.dist_lat_factor = 0.2
		self.dist_lat_offset = -204.6
		self.dist_lat_start_handle = (self.dist_lat_start // 8 + 1) * 8 - self.dist_lat_start % 8 - self.dist_lat_length
		self.verl_long_start = 46
		self.verl_long_length = 10
		self.verl_long_factor = 0.25
		self.verl_long_offset = -128
		self.verl_long_start_handle = (self.verl_long_start // 8 + 1) * 8 - self.verl_long_start % 8 - self.verl_long_length
		self.verl_lat_start = 53
		self.verl_lat_length = 9
		self.verl_lat_factor = 0.25
		self.verl_lat_offset = -64
		self.verl_lat_start_handle = (self.verl_lat_start // 8 + 1) * 8 - self.verl_lat_start % 8 - self.verl_lat_length
		self.dyn_prop_start = 48
		self.dyn_prop_length = 3
		self.dyn_prop_factor = 1
		self.dyn_prop_offset = 0
		self.dyn_prop_start_handle = (self.dyn_prop_start // 8 + 1) * 8 - self.dyn_prop_start % 8 - self.dyn_prop_length
		self.rcs_start = 56
		self.rcs_length = 8
		self.rcs_factor = 0.5
		self.rcs_offset = -64
		self.rcs_start_handle = (self.rcs_start // 8 + 1) * 8 - self.rcs_start % 8 - self.rcs_length

	def open(self):
		result = self.canDLL.OpenDevice(self.Struct_USBCAN2C, 0, 0)
		if result != self.STATUS_OK:
			print('调用 Struct_OpenDevice出错\r\n')

	def init_channel(self, channel):
		result = self.canDLL.InitCAN(self.Struct_USBCAN2C, 0, channel, ctypes.byref(self.struct_initconfig))
		if result != self.STATUS_OK:
			print('调用 Struct_InitCAN' + channel + '出错\r\n')
		result = self.canDLL.StartCAN(self.Struct_USBCAN2C, 0, channel)
		if result != self.STATUS_OK:
			print('调用 Struct_StartCAN' + channel + '出错\r\n')

	def send_message(self, channel):
		byte_array = ctypes.c_ubyte * 8
		information = byte_array(1, 2, 3, 4, 5, 6, 7, 64)
		byte_3array = ctypes.c_ubyte * 3
		remain = byte_3array(0, 0, 0)
		can_obj = Struct_CAN_OBJ(0x0, 0, 0, 1, 0, 0, 8, information, remain)
		result = self.canDLL.Transmit(self.Struct_USBCAN2C, 0, channel, ctypes.byref(can_obj), 1)
		if result != self.STATUS_OK:
			print('调用 Struct_Transmit 出错\r\n')

	def get_message(self, channel):
		# 接收通道数据
		byte_array = ctypes.c_ubyte * 8
		information = byte_array(0, 0, 0, 0, 0, 0, 0, 1)
		byte_3array = ctypes.c_ubyte * 3
		remain = byte_3array(0, 0, 0)
		self.can_obj = Struct_CAN_OBJ(0x0, 1, 1, 0, 0, 0, 8, information, remain)
		ret = self.canDLL.Receive(self.Struct_USBCAN2C, 0, channel, ctypes.byref(self.can_obj), 1, 1)
		if ret > 0:
			if self.can_obj.ID == 1547:
				# start = time.clock()
				struct_can_obj_data = list(self.can_obj.Data)
				# print(self.can_obj.TimeStamp)
				message = ''
				# 16进制转化为2进制
				for i in struct_can_obj_data:
					bin_i = bin(i)
					# 每比特转化成2进制，空位补零
					bin_i = bin_i[2:].rjust(8, '0')
					message += bin_i
				# 根据DBC文件取ID
				obj_id_bin = message[self.id_start_handle:self.id_start_handle + self.id_length]
				obj_dist_long_bin = message[self.dist_long_start_handle:self.dist_long_start_handle + self.dist_long_length]
				obj_dist_lat_bin = message[self.dist_lat_start_handle:self.dist_lat_start_handle + self.dist_lat_length]
				obj_verl_long_bin = message[self.verl_long_start_handle:self.verl_long_start_handle + self.verl_long_length]
				obj_verl_lat_bin = message[self.verl_lat_start_handle:self.verl_lat_start_handle + self.verl_lat_length]
				obj_dyn_prop_bin = message[self.dyn_prop_start_handle:self.dyn_prop_start_handle + self.dyn_prop_length]
				obj_rcs_bin = message[self.rcs_start_handle:self.rcs_start_handle + self.rcs_length]
				obj_id = int(obj_id_bin, 2) * self.id_factor + self.id_offset
				# 将截取的二进制数据转化为十进制
				obj_dist_long = int(obj_dist_long_bin, 2) * self.dist_long_factor + self.dist_long_offset
				obj_dist_lat = int(obj_dist_lat_bin, 2) * self.dist_lat_factor + self.dist_lat_offset
				obj_verl_long = int(obj_verl_long_bin, 2) * self.verl_long_factor + self.verl_long_offset
				obj_verl_lat = int(obj_verl_lat_bin, 2) * self.verl_lat_factor + self.verl_lat_offset
				obj_dyn_prop = int(obj_dyn_prop_bin, 2) * self.dyn_prop_factor + self.dyn_prop_offset
				obj_rcs = int(obj_rcs_bin, 2) * self.rcs_factor + self.rcs_offset
				self.data = [obj_id, round(obj_dist_long, 2), round(obj_dist_lat, 2), obj_verl_long, obj_verl_lat, obj_rcs, obj_dyn_prop]
				# 定义数据为新数据
				# message_status = 1
				# for i in range(len(self.data)):
				#     if self.data[i, 0] == data_basic[0]:
				#         self.data[i] = data_basic
				# print('数据刷新')
				# 数据状态更新
				# message_status = 0
				# if message_status == 1:
				#     self.data = np.row_stack((self.data, data_basic))
					# print('数据新增')
				# print(self.data)
				# end = time.clock()
				# print(round(end-start, 3))

	def close(self):
		result = self.canDLL.CloseDevice(self.Struct_USBCAN2C, 0)
		if result != self.STATUS_OK:
			print('调用 Struct_CloseDevice出错\r\n')


class CanFDControl:
	def __init__(self):
		self.canDLL = ctypes.CDLL('./dll/zlgcan.dll')

	pass


if __name__ == '__main__':
	can_control = CanControl()
	can_control.open()
	can_control.init_channel(0)
	while True:
		can_control.get_message(0)
		print(can_control.data)
