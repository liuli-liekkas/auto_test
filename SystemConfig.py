from MachineClass import *
from UIRadarTest import *
import time
# import winsound
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class HorizontalPowerTest(RadarTestMain):
	def __init__(self):
		super(HorizontalPowerTest, self).__init__()
		self.tab2_test_start_button.clicked.connect(self.get_message)
		self.my_thread = MyThread()
		self.my_thread.my_signal.connect(self.set_label)

		# turn_table = TurnTable()
		# target_simulate = ARTS()

	def get_config(self):
		self.horizontal_power_menu = HorizontalPowerMenu()
		self.horizontal_power_test_config_file = open('./config/HorizontalPowerTest.txt', 'r')
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

	def show_config(self):
		self.tab2_status_test_edit.append(
			'------开始测试--水平探测威力------' + '   ' + time.strftime('%H:%M:%S') + '\n'
			'目标RCS设置为:%sdBsm\n'
			'最小测试距离设置为：%sm\n'
			'最大测试距离设置为：%sm\n'
			'最小测试角度设置为：%s°\n'
			'最大测试角度设置为：%s°\n'
			'步进距离设置为：%sm\n'
			'步进角度设置为：%sm\n'
			'驻留时间设置为：%ss\n'
			'运动模式设置为：%s\n'
			'单向运动模式设置为：%s\n'
			'测试模式设置为：%s\n' % (
				self.target_rcs_config,
				self.min_range_config,
				self.max_range_config,
				self.min_angle_config,
				self.max_angle_config,
				self.step_range_config,
				self.step_angle_config,
				self.dwell_time_config,
				self.motor_pattern_config,
				self.motor_pattern_one_way_config,
				self.test_mode_config))

	def set_label(self, message):
		self.tab2_status_test_edit.append(message)
		# self.tab2_status_test_edit.moveCursor(TextEdit.textCursor().End)

	def get_message(self):
		self.my_thread.start()


class MyThread(QThread):
	my_signal = pyqtSignal(str)

	def __init__(self):
		super(MyThread, self).__init__()

	def run(self):
		# 从配置文件获得配置信息
		self.horizontal_power_menu = HorizontalPowerMenu()
		self.turn_table = TurnTable()
		self.turn_table.connect()
		self.target_simulate = ARTS()
		self.target_simulate.connect('192.168.0.20')
		self.horizontal_power_test_config_file = open('./config/HorizontalPowerTest.txt', 'r')
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
		self.my_signal.emit('------转台位置初始化，开始测试------' + time.strftime('%H:%M:%S'))
		self.target_simulate.set_mode_static()
		self.target_simulate.set_tx_chan_enable(1, 0, 0, 0)
		self.target_simulate.set_tr_on()
		self.target_simulate.set_output_on()
		if self.test_mode_config == '先距离后角度':
			for anger in range(self.min_angle_config, self.max_angle_config + 1, self.step_angle_config):
				self.turn_table.move_to_position(2, anger, 1)
				self.my_signal.emit(
					'------当前角度：' + str(anger) + '°' + '------' + time.strftime('%H:%M:%S'))
				self.turn_table.get_position(2)
				for distance in range(self.min_range_config, self.max_range_config + 1, self.step_range_config):
					self.target_simulate.set_tx_chan_static(0, 0, 0, 0, -10, -10, -10, -10, distance, distance, distance, distance)
					self.my_signal.emit(
						'------当前距离：' + str(distance) + 'm' + '------' + time.strftime('%H:%M:%S'))
					self.sleep(self.dwell_time_config)
					# winsound.Beep(600, 1000)
			self.target_simulate.disconnect()
		elif self.test_mode_config == '先角度后距离':
			print('先角度后距离')
		else:
			print('测试模式错误')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	HorizontalPowerTest = HorizontalPowerTest()
	HorizontalPowerTest.show()
	sys.exit(app.exec_())
