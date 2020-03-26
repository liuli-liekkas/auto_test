from MachineClass import *
from UIRadarTest import *
import time
# import winsound
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QThread


class HorizontalPowerTest(RadarTestMain):
    def __init__(self):
        super(HorizontalPowerTest, self).__init__()
        self.tab2_test_start_button.clicked.connect(self.start_test)
        # turn_table = TurnTable()
        # target_simulate = ARTS()

    def get_config(self):
        self.horizontal_power_menu = HorizontalPowerMenu()
        print()
        # self.horizontal_power_test_config_file = open('./config/HorizontalPowerTest.txt', 'r')
        # self.horizontal_power_test_config = self.horizontal_power_test_config_file.readlines()
        # self.target_rcs_config = float(self.horizontal_power_test_config[0].split(':')[1][0:-5])
        # self.min_range_config = float(self.horizontal_power_test_config[1].split(':')[1][0:-2])
        # self.max_range_config = float(self.horizontal_power_test_config[2].split(':')[1][0:-2])
        # self.min_angle_config = float(self.horizontal_power_test_config[3].split(':')[1][0:-2])
        # self.max_angle_config = float(self.horizontal_power_test_config[4].split(':')[1][0:-2])
        # self.step_range_config = float(self.horizontal_power_test_config[5].split(':')[1][0:-2])
        # self.step_angle_config = float(self.horizontal_power_test_config[6].split(':')[1][0:-2])
        # self.dwell_time_config = int(self.horizontal_power_test_config[7].split(':')[1][0:-2])
        # self.motor_pattern_config = self.horizontal_power_test_config[8].split(':')[1][0:-1]
        # self.motor_pattern_one_way_config = self.horizontal_power_test_config[9].split(':')[1][0:-1]
        # self.test_mode_config = self.horizontal_power_test_config[10].split(':')[1][0:-1]

    def show_config(self):
        self.tab2_status_test_edit.setPlainText(
              self.tab2_status_test_edit.toPlainText() +
              '------开始测试--水平探测威力------\n'
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

    def start_test(self):
        self.get_config()
        self.show_config()
        if self.test_mode_config == '先距离后角度':
            print('先距离后角度')

        elif self.test_mode_config == '先角度后距离':
            print('先角度后距离')
        else:
            print('测试模式错误')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    HorizontalPowerTest = HorizontalPowerTest()
    HorizontalPowerTest.show()
    sys.exit(app.exec_())



