from PyQt5.QtCore import QThread, pyqtSignal
from MachineClass import *
import time


# class Connect

class CurrentAngleAzimuth(QThread):
	my_signal = pyqtSignal(str)

	def __init__(self):
		super(CurrentAngleAzimuth, self).__init__()

	def run(self):
		self.turn_table = TurnTable()
		self.turn_table.connect()
		self.msleep(100)
		while True:
			self.my_signal.emit(str(round(self.turn_table.get_position(2), 2)))
			self.msleep(100)


class CurrentAnglePitching(QThread):
	my_signal = pyqtSignal(str)

	def __init__(self):
		super(CurrentAnglePitching, self).__init__()

	def run(self):
		self.turn_table = TurnTable()
		self.turn_table.connect()
		self.msleep(100)
		while True:
			self.my_signal.emit(str(round(self.turn_table.get_position(1), 2)))
			self.msleep(100)


class FindHome(QThread):
	my_signal = pyqtSignal(str)

	def __init__(self, n_axis):
		super(FindHome, self).__init__()
		self.n_axis = n_axis

	def run(self):
		self.turn_table = TurnTable()
		self.turn_table.connect()
		self.msleep(100)
		while True:
			self.status = self.turn_table.get_home_complete(self.n_axis)
			if self.status == 1:
				if self.n_axis == 2:
					self.my_signal.emit('水平寻零结束')
				else:
					self.my_signal.emit('俯仰寻零结束')
				break
			self.msleep(100)


class TurnTableInitialize(QThread):
	my_signal = pyqtSignal(bool)

	def __init__(self, n_axis):
		super(TurnTableInitialize, self).__init__()
		self.n_axis = n_axis

	def run(self):
		self.turn_table = TurnTable()
		self.turn_table.connect()
		self.msleep(100)
		while True:
			self.status = self.turn_table.get_motor_idle(self.n_axis)
			if self.status == 1:
				if self.n_axis == 2:
					self.my_signal.emit('水平初始化到位')
				else:
					self.my_signal.emit('俯仰初始化到位')
				break
			self.msleep(100)


class GetMessage(QThread):
	my_signal = pyqtSignal(list)

	def __init__(self):
		super(GetMessage, self).__init__()

	def run(self):
		self.can_control = CanControl()
		self.can_control.open()
		self.can_control.init_channel(0)
		self.message = []
		self.time_stamp = 0
		while True:
			self.can_control.get_message(0)
			if self.can_control.can_obj.ID == 1547:
				# print(self.can_control.can_obj.TimeStamp - self.time_stamp)
				if self.can_control.can_obj.TimeStamp - self.time_stamp > 30000:
					self.my_signal.emit(self.message)
					self.message = []
					self.message.append(self.can_control.data)
					self.time_stamp = self.can_control.can_obj.TimeStamp
				elif self.can_control.can_obj.TimeStamp - self.time_stamp <= 30000:
					self.message.append(self.can_control.data)


class HorizontalPowerTest(QThread):
	my_signal = pyqtSignal(str)

	def __init__(self):
		super(HorizontalPowerTest, self).__init__()

	def run(self):
		# 从配置文件获得配置信息
		self.turn_table = TurnTable()
		self.turn_table.connect()
		self.target_simulate = ARTS()
		self.target_simulate.connect('192.168.0.20')
		self.horizontal_power_test_config_file = open('./config/HorizontalPowerTest.txt')
		self.horizontal_power_test_config = self.horizontal_power_test_config_file.readlines()
		self.target_rcs_config = int(self.horizontal_power_test_config[0].split(':')[1][0:-5])
		self.min_range_config = int(self.horizontal_power_test_config[1].split(':')[1][0:-2])
		self.max_range_config = int(self.horizontal_power_test_config[2].split(':')[1][0:-2])
		self.min_angle_config = int(self.horizontal_power_test_config[3].split(':')[1][0:-2])
		self.max_angle_config = int(self.horizontal_power_test_config[4].split(':')[1][0:-2])
		self.step_range_config = int(self.horizontal_power_test_config[5].split(':')[1][0:-2])
		self.step_angle_config = int(self.horizontal_power_test_config[6].split(':')[1][0:-2])
		self.dwell_time_config = int(self.horizontal_power_test_config[7].split(':')[1][0:-2])
		self.motor_pattern_config = self.horizontal_power_test_config[8].split(':')[1][0:-1]
		self.motor_pattern_one_way_config = self.horizontal_power_test_config[9].split(':')[1][0:-1]
		self.test_mode_config = self.horizontal_power_test_config[10].split(':')[1][0:-1]
		self.turn_table.move_to_position(2, self.min_angle_config, 1)
		self.sleep(5)
		# self.my_signal.emit('------转台位置初始化，开始测试------' + time.strftime('%H:%M:%S'), [0, 0])
		self.target_simulate.set_mode_static()
		self.target_simulate.set_tx_chan_enable(1, 0, 0, 0)
		self.target_simulate.set_tr_on()
		self.target_simulate.set_output_on()
		if self.test_mode_config == '先距离后角度':
			for anger in range(self.min_angle_config, self.max_angle_config + 1, self.step_angle_config):
				self.turn_table.move_to_position(2, anger+0.6, 3)
				self.turn_table.get_position(2)
				for distance in range(self.min_range_config, self.max_range_config + 1, self.step_range_config):
					self.target_simulate.set_tx_chan_static(0, 0, 0, 0, -10, -10, -10, -10, distance-2.59, distance-2.59, distance-2.59, distance-2.59)
					time.sleep(3)
					self.my_signal.emit(
						'当前角度{0}°，当前距离：{1}m---{2}---'.format(str(anger), str(distance), time.strftime('%H:%M:%S')), [anger, distance])
					self.sleep(self.dwell_time_config)
					# winsound.Beep(600, 1000)
			self.target_simulate.disconnect()
		elif self.test_mode_config == '先角度后距离':
			print('先角度后距离')
		else:
			print('测试模式错误')
			

if __name__ == '__main__':
	can = GetMessage()
	can.run()
