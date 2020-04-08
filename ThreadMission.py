from PyQt5.QtCore import QThread, pyqtSignal
from MachineClass import *
import cantools


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