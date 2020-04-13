from PyQt5.QtCore import QThread, pyqtSignal
from MachineClass import *
import cantools
from ctypes import wintypes
import ctypes


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


class Struct_INIT_CONFIG(ctypes.Structure):
	_fields_ = (("AccCode", wintypes.DWORD),
                ("AccMask", wintypes.DWORD),
                ("Reserved", wintypes.DWORD),
                ("Filter", ctypes.c_ubyte),
                ("Timing0", ctypes.c_ubyte),
                ("Timing1", ctypes.c_ubyte),
                ("Mode", ctypes.c_ubyte)
                )


class Struct_CAN_OBJ(ctypes.Structure):
    _fields_ = [("ID", ctypes.c_uint),
                ("TimeStamp", ctypes.c_uint),
                ("TimeFlag", ctypes.c_ubyte),
                ("SendType", ctypes.c_ubyte),
                ("RemoteFlag", ctypes.c_ubyte),
                ("ExternFlag", ctypes.c_ubyte),
                ("DataLen", ctypes.c_ubyte),
                ("Data", ctypes.c_ubyte * 8),
                ("Reserved", ctypes.c_ubyte * 3)
                ]


class CanAnalysis()
