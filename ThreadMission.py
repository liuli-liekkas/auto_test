from PyQt5.QtCore import QThread, pyqtSignal
from MachineClass import *
import CanAnalysis


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
		self.can_control = CanAnalysis.CanControl()
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


if __name__ == '__main__':
	can = GetMessage()
	can.run()
