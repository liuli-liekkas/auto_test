from MachineClass import *
from UIRadarTest import *
import time
import math
# import winsound
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class HorizontalPowerTest(RadarTestMain):
	def __init__(self):
		super(HorizontalPowerTest, self).__init__()
		self.tab2_test_start_button.clicked.connect(self.start_test)
		self.my_thread = MyThread()
		self.my_thread.my_signal.connect(self.message_detail)

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
			'步进角度设置为：%s°\n'
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

	def message_detail(self, message_str, message_list):
		self.tab2_status_test_edit.append(message_str)
		if len(self.message) > 1:
			test_validity = 'True'
		else:
			test_validity = 'False'
		# print(self.message)
		# print(message_list)
		new_message = []
		for i in range(len(self.message)):
			if abs(self.message[i][1] - message_list[1]) < 5:
				new_message = self.message[i]
		# print(new_message)
		if new_message:
			delta_anger = message_list[0] - math.degrees(math.atan(new_message[2] / new_message[1]))
			delta_distance = message_list[1] - new_message[1]
		# print(delta_anger, delta_distance)
			self.tab2_status_test_edit.append(
				'测试有效性：{0},角度测量误差：{1}°,距离测量误差：{2}m'.
				format(test_validity, round(delta_anger, 2), round(delta_distance, 2)))
		
	def start_test(self):
		self.my_thread.start()


class MyThread(QThread):
	my_signal = pyqtSignal(str, list)

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
	app = QApplication(sys.argv)
	HorizontalPowerTest = HorizontalPowerTest()
	HorizontalPowerTest.show()
	sys.exit(app.exec_())
