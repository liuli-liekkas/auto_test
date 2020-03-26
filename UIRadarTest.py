from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import pyqtgraph as pg
from MachineClass import *


class RadarTestMain(QMainWindow):
	def __init__(self):
		super(RadarTestMain, self).__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(1200, 800)
		self.center()
		self.setWindowTitle("毫米波雷达测试系统")
		# self.setFont(QFont('Menlo', 12))
		self.menu_init()
		# self.tool_menu_init()
		self.tab_menu_init()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def menu_init(self):
		menubar = self.menuBar()
		file_menu = menubar.addMenu("文件")
		mission_menu = menubar.addMenu("任务")
		view_menu = menubar.addMenu("视图")
		config_menu = menubar.addMenu("配置")
		analysis_menu = menubar.addMenu("分析")
		self_test_menu = menubar.addMenu("自检")
		tool_menu = menubar.addMenu("工具")
		help_menu = menubar.addMenu("帮助")
		# 文件菜单
		open_act = QAction("打开", self)
		open_act.setShortcut('Ctrl+O')
		open_act.triggered.connect(lambda: QFileDialog.getOpenFileName(self, '打开文件', '/home'))
		file_menu.addAction(open_act)
		save_act = QAction("保存", self)
		save_act.setShortcut('Ctrl+S')
		save_act.triggered.connect(self.save_file)
		file_menu.addAction(save_act)
		exit_act = QAction("退出", self)
		exit_act.setShortcut("Ctrl+Q")
		exit_act.triggered.connect(qApp.quit)
		file_menu.addAction(exit_act)
		# 任务菜单
		new_mission_act = QAction('新建', self)
		mission_menu.addAction(new_mission_act)
		edit_mission_act = QAction('修改', self)
		mission_menu.addAction(edit_mission_act)
		# 配置菜单
		power_supply_act = QAction('电源', self)
		power_supply_act.triggered.connect(self.power_supply_config)
		config_menu.addAction(power_supply_act)
		frequency_analysis_act = QAction('频谱仪', self)
		config_menu.addAction(frequency_analysis_act)
		signal_source_act = QAction('信号源', self)
		config_menu.addAction(signal_source_act)
		oscilloscope_act = QAction('示波器', self)
		config_menu.addAction(oscilloscope_act)
		target_simulate_act = QAction('目标模拟器', self)
		config_menu.addAction(target_simulate_act)
		turn_table_act = QAction('转台', self)
		config_menu.addAction(turn_table_act)
		turn_table_act.triggered.connect(self.turn_table_config)
		# 工具菜单
		com_act = QAction("串口调试", self)
		# com_act.triggered.connect()
		tool_menu.addAction(com_act)
		net_act = QAction("网口调试", self)
		# net_act.triggered.connect()
		tool_menu.addAction(net_act)

	def open_file(self):
		QFileDialog.getOpenFileName(self, '打开文件', '/home')

	def save_file(self):
		QFileDialog.getSaveFileName(self, '保存文件', '/home')

	def tool_menu_init(self):
		exit_act = QAction("退出", self)
		exit_act.setShortcut("Ctrl+Q")
		exit_act.triggered.connect(qApp.quit)
		exit_act.setToolTip("退出应用")

		self.toolbar = self.addToolBar("exit")
		self.toolbar.addAction(exit_act)

	def tab_menu_init(self):
		self.central_widget = QWidget()
		self.tabWidget = QTabWidget(self.central_widget)
		self.tabWidget.setGeometry(0, 0, self.geometry().width(), self.geometry().height() - 50)
		self.tabWidget.setStyleSheet("QTabBar::tab:selected{color:red;background-color:rbg(200,200,255);} ")
		self.tabWidget.setFont(QFont('KaiTi', 16))
		self.tab1_central_widget = QWidget()
		self.tab2_central_widget = QWidget()
		self.tab3_central_widget = QWidget()
		self.tabWidget.addTab(self.tab1_central_widget, "射频性能测试")
		self.tabWidget.addTab(self.tab2_central_widget, "探测性能测试")
		self.tabWidget.addTab(self.tab3_central_widget, "天线性能测试")
		self.setCentralWidget(self.central_widget)
		self.tab1_ui()
		self.tab2_ui()
		self.tab3_ui()

	def tab1_ui(self):
		pass

	def tab1_layout_init(self):
		pass

	def tab2_ui(self):
		# 基本信息
		self.left_frame = QFrame(self.tab2_central_widget)
		self.middle_frame = QFrame(self.tab2_central_widget)
		self.right_frame = QFrame(self.tab2_central_widget)
		self.tab2_sample_number_label = QLabel(self.left_frame)
		self.tab2_sample_number_label.setText('样品编号:')
		self.tab2_sample_number_browser = QTextBrowser()
		self.tab2_sample_number_browser.setText('00001')
		self.tab2_sample_number_browser.setMinimumSize(80, 20)
		self.tab2_sample_number_browser.setMaximumSize(100, 20)
		self.tab2_tester_name_label = QLabel('测试人员:')
		self.tab2_tester_name_browser = QTextBrowser()
		self.tab2_tester_name_browser.setText('薛岩')
		self.tab2_tester_name_browser.setMinimumSize(80, 20)
		self.tab2_tester_name_browser.setMaximumSize(100, 20)
		self.tab2_supervisor_name_label = QLabel('复核/监督人员:')
		self.tab2_supervisor_name_combo = QComboBox()
		self.tab2_supervisor_name_combo.setMaximumSize(80, 20)
		self.tab2_supervisor_name_combo.addItem('刘力')
		self.tab2_supervisor_name_combo.addItem('申亚飞')
		self.tab2_supervisor_name_combo.addItem('裴毓')
		self.tab2_supervisor_name_combo.addItem('张晓蕾')
		self.tab2_supervisor_name_combo.addItem('薛岩')
		self.tab2_test_data_label = QLabel('试验日期')
		self.tab2_test_data_edit = QDateEdit()
		self.tab2_test_data_edit.setMaximumSize(200, 20)
		self.tab2_test_data_edit.setCalendarPopup(True)
		self.tab2_test_data_edit.setDate(QtCore.QDate(2020, 1, 1))
		# 测试内容
		self.tab2_horizontal_power_box = QCheckBox('水平探测威力')
		self.tab2_vertical_power_box = QCheckBox('垂直探测威力')
		self.tab2_distance_resolution_box = QCheckBox('距离分辨率')
		self.tab2_distance_distinction_box = QCheckBox('距离区分度')
		self.tab2_horizontal_angular_range_box = QCheckBox('水平角度范围')
		self.tab2_vertical_angular_range_box = QCheckBox('垂直角度范围')
		self.tab2_angular_resolution_box = QCheckBox('角度分辨率')
		self.tab2_horizontal_distinction_box = QCheckBox('角度区分度')
		self.tab2_speed_range_box = QCheckBox('速度范围')
		self.tab2_speed_resolution_box = QCheckBox('速度分辨率')
		self.tab2_speed_distinction_box = QCheckBox('速度区分度')
		self.tab2_test_start_button = QPushButton('开始测试')
		self.tab2_test_pause_button = QPushButton('暂停测试')
		self.tab2_test_stop_button = QPushButton('终止测试')
		self.tab2_horizontal_power_config_button = QPushButton('设置')
		self.tab2_horizontal_power_config_button.setEnabled(False)
		self.tab2_horizontal_power_config_button.clicked.connect(self.horizontal_power_config_window)
		self.tab2_horizontal_power_box.stateChanged.connect(self.tab2_horizontal_power_button_status)
		self.tab2_vertical_power_config_button = QPushButton('设置')
		self.tab2_vertical_power_config_button.setEnabled(False)
		self.tab2_vertical_power_box.stateChanged.connect(self.tab2_vertical_power_button_status)
		self.tab2_distance_resolution_config_button = QPushButton('设置')
		self.tab2_distance_resolution_config_button.setEnabled(False)
		self.tab2_distance_resolution_box.stateChanged.connect(self.tab2_distance_resolution_button_status)
		self.tab2_distance_distinction_config_button = QPushButton('设置')
		self.tab2_distance_distinction_config_button.setEnabled(False)
		self.tab2_distance_distinction_box.stateChanged.connect(self.tab2_distance_distinction_button_status)
		self.tab2_horizontal_angular_range_config_button = QPushButton('设置')
		self.tab2_horizontal_angular_range_config_button.setEnabled(False)
		self.tab2_horizontal_angular_range_box.stateChanged.connect(self.tab2_horizontal_angular_range_button_status)
		self.tab2_vertical_angular_range_config_button = QPushButton('设置')
		self.tab2_vertical_angular_range_config_button.setEnabled(False)
		self.tab2_vertical_angular_range_box.stateChanged.connect(self.tab2_vertical_angular_range_button_status)
		self.tab2_angular_resolution_config_button = QPushButton('设置')
		self.tab2_angular_resolution_config_button.setEnabled(False)
		self.tab2_angular_resolution_box.stateChanged.connect(self.tab2_angular_resolution_button_status)
		self.tab2_horizontal_distinction_config_button = QPushButton('设置')
		self.tab2_horizontal_distinction_config_button.setEnabled(False)
		self.tab2_horizontal_distinction_box.stateChanged.connect(self.tab2_horizontal_distinction_button_status)
		self.tab2_speed_range_config_button = QPushButton('设置')
		self.tab2_speed_range_config_button.setEnabled(False)
		self.tab2_speed_range_box.stateChanged.connect(self.tab2_speed_range_button_status)
		self.tab2_speed_resolution_config_button = QPushButton('设置')
		self.tab2_speed_resolution_config_button.setEnabled(False)
		self.tab2_speed_resolution_box.stateChanged.connect(self.tab2_speed_resolution_button_status)
		self.tab2_speed_distinction_config_button = QPushButton('设置')
		self.tab2_speed_distinction_config_button.setEnabled(False)
		self.tab2_speed_distinction_box.stateChanged.connect(self.tab2_speed_distinction_button_status)
		# 状态信息
		self.tab2_status_test_label = QLabel('测试状态')
		self.tab2_status_test_edit = QTextEdit()
		self.tab2_status_test_edit.setStyleSheet('background-color:white;font-size:12px')
		self.tab2_result_test_label = QLabel('试验结果')
		self.tab2_result_test_edit = QTextEdit()
		# 雷达目标信息
		self.tab2_realtime_plot = pg.PlotWidget()
		self.tab2_realtime_plot.showGrid(x=True, y=True)
		self.tab2_realtime_plot.setRange(xRange=[-5, 5], yRange=[0, 300])
		self.tab2_realtime_table = QTableWidget()
		self.tab2_realtime_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.tab2_realtime_table.setColumnCount(6)
		self.tab2_realtime_table.setRowCount(10)
		self.tab2_realtime_table.setHorizontalHeaderLabels(['ID', '垂直距离', '水平距离', '方位角度', '相对速度', '目标RCS'])
		# 位置初始化
		self.tab2_layout_init()

	def tab2_layout_init(self):
		# ---底层界面布局---
		# 左侧顶层布局
		self.tab2_lu_h_layout = QHBoxLayout()
		self.tab2_lu_h_layout.addWidget(self.tab2_sample_number_label)
		self.tab2_lu_h_layout.addWidget(self.tab2_sample_number_browser)
		self.tab2_lu_h_layout.addWidget(self.tab2_tester_name_label)
		self.tab2_lu_h_layout.addWidget(self.tab2_tester_name_browser)
		self.tab2_lu_h_layout.addWidget(self.tab2_supervisor_name_label)
		self.tab2_lu_h_layout.addWidget(self.tab2_supervisor_name_combo)
		self.tab2_lu_h_layout.addWidget(self.tab2_test_data_label)
		self.tab2_lu_h_layout.addWidget(self.tab2_test_data_edit)
		# 左侧底部L布局
		self.tab2_ldl_grid_layout = QGridLayout()
		self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_power_box, 0, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_power_config_button, 0, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_vertical_power_box, 1, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_vertical_power_config_button, 1, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_distance_resolution_box, 2, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_distance_resolution_config_button, 2, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_distance_distinction_box, 3, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_distance_distinction_config_button, 3, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_angular_range_box, 4, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_angular_range_config_button, 4, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_vertical_angular_range_box, 5, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_vertical_angular_range_config_button, 5, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_distinction_box, 6, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_horizontal_distinction_config_button, 6, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_range_box, 7, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_range_config_button, 7, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_resolution_box, 8, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_resolution_config_button, 8, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_distinction_box, 9, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_speed_distinction_config_button, 9, 2, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_test_start_button, 10, 0, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_test_pause_button, 10, 1, 1, 1)
		self.tab2_ldl_grid_layout.addWidget(self.tab2_test_stop_button, 10, 2, 1, 1)
		# 左侧底部R布局
		self.tab2_ldr_v_layout = QVBoxLayout()
		self.tab2_ldr_v_layout.addWidget(self.tab2_status_test_label)
		self.tab2_ldr_v_layout.addWidget(self.tab2_status_test_edit)
		self.tab2_ldr_v_layout.addWidget(self.tab2_result_test_label)
		self.tab2_ldr_v_layout.addWidget(self.tab2_result_test_edit)
		self.tab2_ldr_v_layout.addWidget(self.tab2_realtime_table)
		# 左侧底部布局
		self.tab2_ld_h_layout = QHBoxLayout()
		self.tab2_ld_h_layout.addLayout(self.tab2_ldl_grid_layout)
		self.tab2_ld_h_layout.addLayout(self.tab2_ldr_v_layout)
		# 右侧布局
		self.tab2_right_v_layout = QVBoxLayout()
		self.tab2_right_v_layout.addWidget(self.tab2_realtime_plot)
		# 左侧布局
		self.tab2_left_v_layout = QVBoxLayout()
		self.tab2_left_v_layout.addLayout(self.tab2_lu_h_layout)
		self.tab2_left_v_layout.addLayout(self.tab2_ld_h_layout)
		# 完整布局
		self.all_h_layout = QHBoxLayout()
		self.all_h_layout.addLayout(self.tab2_left_v_layout)
		self.all_h_layout.addLayout(self.tab2_right_v_layout)
		self.tab2_central_widget.setLayout(self.all_h_layout)

	def tab2_horizontal_power_button_status(self):
		if self.tab2_horizontal_power_box.checkState() == 2:
			self.tab2_horizontal_power_config_button.setEnabled(True)
		else:
			self.tab2_horizontal_power_config_button.setEnabled(False)

	def tab2_vertical_power_button_status(self):
		if self.tab2_vertical_power_box.checkState() == 2:
			self.tab2_vertical_power_config_button.setEnabled(True)
		else:
			self.tab2_vertical_power_config_button.setEnabled(False)

	def tab2_distance_resolution_button_status(self):
		if self.tab2_distance_resolution_box.checkState() == 2:
			self.tab2_distance_resolution_config_button.setEnabled(True)
		else:
			self.tab2_distance_resolution_config_button.setEnabled(False)

	def tab2_distance_distinction_button_status(self):
		if self.tab2_distance_distinction_box.checkState() == 2:
			self.tab2_distance_distinction_config_button.setEnabled(True)
		else:
			self.tab2_distance_distinction_config_button.setEnabled(False)

	def tab2_horizontal_angular_range_button_status(self):
		if self.tab2_horizontal_angular_range_box.checkState() == 2:
			self.tab2_horizontal_angular_range_config_button.setEnabled(True)
		else:
			self.tab2_horizontal_angular_range_config_button.setEnabled(False)

	def tab2_vertical_angular_range_button_status(self):
		if self.tab2_vertical_angular_range_box.checkState() == 2:
			self.tab2_vertical_angular_range_config_button.setEnabled(True)
		else:
			self.tab2_vertical_angular_range_config_button.setEnabled(False)

	def tab2_angular_resolution_button_status(self):
		if self.tab2_angular_resolution_box.checkState() == 2:
			self.tab2_angular_resolution_config_button.setEnabled(True)
		else:
			self.tab2_angular_resolution_config_button.setEnabled(False)

	def tab2_horizontal_distinction_button_status(self):
		if self.tab2_horizontal_distinction_box.checkState() == 2:
			self.tab2_horizontal_distinction_config_button.setEnabled(True)
		else:
			self.tab2_horizontal_distinction_config_button.setEnabled(False)

	def tab2_speed_range_button_status(self):
		if self.tab2_speed_range_box.checkState() == 2:
			self.tab2_speed_range_config_button.setEnabled(True)
		else:
			self.tab2_speed_range_config_button.setEnabled(False)

	def tab2_speed_resolution_button_status(self):
		if self.tab2_speed_resolution_box.checkState() == 2:
			self.tab2_speed_resolution_config_button.setEnabled(True)
		else:
			self.tab2_speed_resolution_config_button.setEnabled(False)

	def tab2_speed_distinction_button_status(self):
		if self.tab2_speed_distinction_box.checkState() == 2:
			self.tab2_speed_distinction_config_button.setEnabled(True)
		else:
			self.tab2_speed_distinction_config_button.setEnabled(False)

	def power_supply_config(self):
		self.power_supply = PowerSupplyConfig()
		self.power_supply.show()

	def turn_table_config(self):
		self.turn_table = TurnTableConfig()
		self.turn_table.show()

	def horizontal_power_config_window(self):
		self.horizontal_power_config_menu_window = HorizontalPowerMenu()
		self.horizontal_power_config_menu_window.show()
		self.horizontal_power_config_menu_window.confirm_button.clicked.connect(
			self.horizontal_power_config_confirm)

	def horizontal_power_config_confirm(self):
		if self.horizontal_power_config_menu_window.motor_pattern_round_trip_button.isChecked():
			motor_pattern = '往返运动'
			motor_pattern_one_way = '无效'
		else:
			motor_pattern = '单向运动'
			motor_pattern_one_way = self.horizontal_power_config_menu_window.motor_pattern_one_way_combo.currentText()
		self.tab2_status_test_edit.setPlainText(
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
				self.horizontal_power_config_menu_window.target_rcs_edit.toPlainText(),
				self.horizontal_power_config_menu_window.min_range_edit.toPlainText(),
				self.horizontal_power_config_menu_window.max_range_edit.toPlainText(),
				self.horizontal_power_config_menu_window.min_angle_edit.toPlainText(),
				self.horizontal_power_config_menu_window.max_angle_edit.toPlainText(),
				self.horizontal_power_config_menu_window.step_range_edit.toPlainText(),
				self.horizontal_power_config_menu_window.step_angle_edit.toPlainText(),
				self.horizontal_power_config_menu_window.dwell_time_edit.toPlainText(),
				motor_pattern,
				motor_pattern_one_way,
				self.horizontal_power_config_menu_window.test_mode_combo.currentText()))
		self.horizontal_power_config_menu_window.close()

	def tab3_ui(self):
		pass


class HorizontalPowerMenu(QWidget):
	def __init__(self):
		super(HorizontalPowerMenu, self).__init__()
		self.file = open('./config/HorizontalPowerTest.txt', 'r', encoding='unicode_escape')
		self.edit_result = self.file.readlines()
		self.resize(200, 200)
		self.setWindowTitle('水平威力范围设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
		self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		self.dwell_time_edit.setMaximumSize(50, 25)
		self.dwell_time_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.dwell_time_unit_label = QLabel('s')
		self.motor_pattern_one_way_button = QRadioButton('单向运动')
		self.motor_pattern_round_trip_button = QRadioButton('往返运动')
		self.motor_pattern_round_trip_button.setChecked(True)
		self.motor_pattern_round_trip_button.toggled.connect(self.radiobutton_select)
		self.motor_pattern_one_way_combo = QComboBox()
		self.motor_pattern_one_way_combo.addItems(('远离', '靠近'))
		self.motor_pattern_one_way_combo.setEnabled(False)
		self.test_mode_combo = QComboBox()
		self.test_mode_combo.addItems(('先距离后角度', '先角度后距离'))
		self.confirm_button = QPushButton('确认')
		self.confirm_button.clicked.connect(self.confirm_config)
		self.layout_init()

	def layout_init(self):
		self.grid_layout = QGridLayout()
		self.h_layout = QHBoxLayout()
		self.v_layout = QVBoxLayout()
		self.grid_layout.addWidget(self.target_rcs_label, 0, 0, 1, 1)
		self.grid_layout.addWidget(self.target_rcs_edit, 0, 1, 1, 2)
		self.grid_layout.addWidget(self.target_rcs_unit_label, 0, 3, 1, 1)
		self.grid_layout.addWidget(self.min_range_label, 1, 0, 1, 1)
		self.grid_layout.addWidget(self.min_range_edit, 1, 1, 1, 2)
		self.grid_layout.addWidget(self.min_range_unit_label, 1, 3, 1, 1)
		self.grid_layout.addWidget(self.max_range_label, 2, 0, 1, 1)
		self.grid_layout.addWidget(self.max_range_edit, 2, 1, 1, 2)
		self.grid_layout.addWidget(self.max_range_unit_label, 2, 3, 1, 1)
		self.grid_layout.addWidget(self.min_angle_label, 3, 0, 1, 1)
		self.grid_layout.addWidget(self.min_angle_edit, 3, 1, 1, 2)
		self.grid_layout.addWidget(self.min_angle_unit_label, 3, 3, 1, 1)
		self.grid_layout.addWidget(self.max_angle_label, 4, 0, 1, 1)
		self.grid_layout.addWidget(self.max_angle_edit, 4, 1, 1, 2)
		self.grid_layout.addWidget(self.max_angle_unit_label, 4, 3, 1, 1)
		self.grid_layout.addWidget(self.step_range_label, 5, 0, 1, 1)
		self.grid_layout.addWidget(self.step_range_edit, 5, 1, 1, 2)
		self.grid_layout.addWidget(self.step_range_unit_label, 5, 3, 1, 1)
		self.grid_layout.addWidget(self.step_angle_label, 6, 0, 1, 1)
		self.grid_layout.addWidget(self.step_angle_edit, 6, 1, 1, 2)
		self.grid_layout.addWidget(self.step_angle_unit_label, 6, 3, 1, 1)
		self.grid_layout.addWidget(self.dwell_time_label, 7, 0, 1, 1)
		self.grid_layout.addWidget(self.dwell_time_edit, 7, 1, 1, 2)
		self.grid_layout.addWidget(self.dwell_time_unit_label, 7, 3, 1, 1)
		self.v_layout.addWidget(self.motor_pattern_round_trip_button)
		self.v_layout.addWidget(self.motor_pattern_one_way_button)
		self.v_layout.addWidget(self.motor_pattern_one_way_combo)
		self.v_layout.addWidget(self.test_mode_combo)
		self.v_layout.addWidget(self.confirm_button)
		self.h_layout.addLayout(self.grid_layout)
		self.h_layout.addLayout(self.v_layout)
		self.setLayout(self.h_layout)

	def radiobutton_select(self):
		if self.motor_pattern_round_trip_button.isChecked():
			self.motor_pattern_one_way_combo.setEnabled(False)
		else:
			self.motor_pattern_one_way_combo.setEnabled(True)

	def confirm_config(self):
		if self.motor_pattern_round_trip_button.isChecked():
			motor_pattern = '往返运动'
			motor_pattern_one_way = '无效'
		else:
			motor_pattern = '单向运动'
			motor_pattern_one_way = self.motor_pattern_one_way_combo.currentText()
		file = open('./config/HorizontalPowerTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%sm\n'
		           '驻留时间设置为:%ss\n'
		           '运动模式设置为:%s\n'
		           '单向运动模式设置为:%s\n'
		           '测试模式设置为:%s\n' % (
			           self.target_rcs_edit.toPlainText(),
			           self.min_range_edit.toPlainText(),
			           self.max_range_edit.toPlainText(),
			           self.min_angle_edit.toPlainText(),
			           self.max_angle_edit.toPlainText(),
			           self.step_range_edit.toPlainText(),
			           self.step_angle_edit.toPlainText(),
			           self.dwell_time_edit.toPlainText(),
			           motor_pattern,
			           motor_pattern_one_way,
			           self.test_mode_combo.currentText()))


class AddMission(QWidget):
	def __init__(self):
		super(AddMission, self).__init__()

	pass


class PowerSupplyConfig(QWidget):
	def __init__(self):
		super(PowerSupplyConfig, self).__init__()
		self.file = open('./config/PowerSupply.txt', 'r', encoding='unicode_escape')
		self.config_result = self.file.readlines()
		self.setWindowTitle('电源设置')
		self.ip_config_label = QLabel('IP地址:')
		self.ip_config_edit = QTextEdit()
		self.ip_config_edit.setText(self.config_result[0].split(':')[1][0:-1])
		self.ip_config_edit.setMaximumSize(130, 25)
		self.ip_config_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.ip_config_confirm_button = QPushButton('连接')
		self.ip_config_confirm_button.clicked.connect(self.power_supply_connect)
		self.volt_config_label = QLabel('工作电压:')
		self.volt_config_edit = QTextEdit()
		self.volt_config_edit.setText(self.config_result[2].split(':')[1][0:-2])
		self.volt_config_edit.setMaximumSize(50, 25)
		self.volt_config_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.volt_config_unit_label = QLabel('V')
		self.curr_config_label = QLabel('工作电流:')
		self.curr_config_edit = QTextEdit()
		self.curr_config_edit.setText(self.config_result[3].split(':')[1][0:-2])
		self.curr_config_edit.setMaximumSize(50, 25)
		self.curr_config_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.curr_config_unit_label = QLabel('A')
		self.chan_config_label = QLabel('工作通道:')
		self.chan_config_combo = QComboBox()
		self.chan_config_combo.addItems(('1', '2'))
		self.query_button = QPushButton('查询')
		self.query_button.clicked.connect(self.query_result)
		self.confirm_button = QPushButton('确认')
		self.confirm_button.clicked.connect(self.confirm_config)
		self.power_on_button = QPushButton('加电')
		self.power_on_button.clicked.connect(self.power_on)
		self.power_off_button = QPushButton('断电')
		self.power_off_button.clicked.connect(self.power_off)
		self.result_label = QLabel('状态显示')
		self.result_edit = QTextBrowser()
		self.result_edit.setMinimumHeight(300)
		self.layout_init()

	def layout_init(self):
		self.grid_layout = QGridLayout()
		self.h_layout = QHBoxLayout()
		self.v_layout = QVBoxLayout()
		self.grid_layout.addWidget(self.ip_config_label, 0, 0, 1, 1)
		self.grid_layout.addWidget(self.ip_config_edit, 0, 1, 1, 2)
		self.grid_layout.addWidget(self.ip_config_confirm_button, 0, 3, 1, 1)
		self.grid_layout.addWidget(self.chan_config_label, 1, 0, 1, 1)
		self.grid_layout.addWidget(self.chan_config_combo, 1, 1, 1, 2)
		self.grid_layout.addWidget(self.confirm_button, 1, 3, 1, 1)
		self.grid_layout.addWidget(self.volt_config_label, 2, 0, 1, 1)
		self.grid_layout.addWidget(self.volt_config_edit, 2, 1, 1, 1)
		self.grid_layout.addWidget(self.volt_config_unit_label, 2, 2, 1, 1)
		self.grid_layout.addWidget(self.query_button, 2, 3, 1, 1)
		self.grid_layout.addWidget(self.curr_config_label, 3, 0, 1, 1)
		self.grid_layout.addWidget(self.curr_config_edit, 3, 1, 1, 1)
		self.grid_layout.addWidget(self.curr_config_unit_label, 3, 2, 1, 1)
		self.grid_layout.addWidget(self.power_on_button, 3, 3, 1, 1)
		self.grid_layout.addWidget(self.power_off_button, 4, 3, 1, 1)
		self.v_layout.addLayout(self.grid_layout)
		self.v_layout.addWidget(self.result_label)
		self.v_layout.addWidget(self.result_edit)
		self.setLayout(self.v_layout)

	def power_supply_connect(self):
		self.power_supply = HMP()
		self.power_supply.open('192.168.0.105')
		self.result_edit.setText(self.result_edit.toPlainText() + '电源连接成功' + time.strftime('%H:%M:%S') + '\n')
		time.sleep(0.1)
		self.power_supply.reset()

	def confirm_config(self):
		file = open('./config/PowerSupply.txt', 'w+')
		file.write('设置IP地址:%s\n'
		           '设置通道:%s\n'
		           '设置电压:%sV\n'
		           '设置电流:%sA\n' % (
			           self.ip_config_edit.toPlainText(),
			           self.chan_config_combo.currentText(),
			           self.volt_config_edit.toPlainText(),
			           self.curr_config_edit.toPlainText()))
		self.power_supply.select_chan(int(self.chan_config_combo.currentText()))
		time.sleep(0.1)
		self.power_supply.set_volt(int(self.volt_config_edit.toPlainText()))
		time.sleep(0.1)
		self.power_supply.set_curr(int(self.curr_config_edit.toPlainText()))
		time.sleep(2)
		self.result_edit.setText(self.result_edit.toPlainText() + '完成设置通道：' + self.power_supply.return_status_chan() + 'V ' + time.strftime('%H:%M:%S') + '\n')
		self.result_edit.setText(self.result_edit.toPlainText() + '完成设置电压：' + self.power_supply.return_status_volt() + 'V ' + time.strftime('%H:%M:%S') + '\n')
		self.result_edit.setText(self.result_edit.toPlainText() + '完成设置电流：' + self.power_supply.return_status_curr() + 'V ' + time.strftime('%H:%M:%S') + '\n')

	def query_result(self):
		self.result_edit.setText(self.result_edit.toPlainText() + '当前设置通道：' + self.power_supply.return_status_chan() + 'V ' + time.strftime('%H:%M:%S') + '\n')
		self.result_edit.setText(self.result_edit.toPlainText() + '当前设置电压：' + self.power_supply.return_status_volt() + 'V ' + time.strftime('%H:%M:%S') + '\n')
		self.result_edit.setText(self.result_edit.toPlainText() + '当前设置电流：' + self.power_supply.return_status_curr() + 'V ' + time.strftime('%H:%M:%S') + '\n')

	def power_on(self):
		self.power_supply.set_output_on()

	def power_off(self):
		self.power_supply.set_output_off()


class TurnTableConfig(QWidget):
	def __init__(self):
		super(TurnTableConfig, self).__init__()
		self.file = open('./config/TurnTable.txt', 'r', encoding='unicode_escape')
		self.config_result = self.file.readlines()
		self.turn_table = TurnTable()
		self.setWindowTitle('转台设置')
		self.group_box_1 = QGroupBox('控制方式')
		self.auto_config_button = QRadioButton('自动设置')
		self.manual_config_button = QRadioButton('手动设置')
		self.manual_config_button.setChecked(True)
		self.manual_config_button.toggled.connect(self.mode_select)
		self.relative_motion_label = QLabel('相对移动')
		self.absolute_motion_label = QLabel('绝对移动')
		self.group_box_2 = QGroupBox('移动方式')
		self.relative_motion_button = QRadioButton('相对移动')
		self.absolute_motion_button = QRadioButton('绝对移动')
		self.relative_motion_button.setChecked(True)
		self.relative_motion_button.toggled.connect(self.mode_select)
		self.current_angle_label = QLabel('当前角度')
		self.azimuth_motion_label = QLabel('方位')
		self.azimuth_relative_edit = QTextEdit()
		self.azimuth_relative_edit.setMaximumSize(50, 25)
		self.azimuth_relative_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.azimuth_relative_edit.setText(self.config_result[2].split(':')[1][0:-3])
		self.azimuth_relative_unit_label = QLabel('°')
		self.azimuth_absolute_edit = QTextEdit()
		self.azimuth_absolute_edit.setMaximumSize(50, 25)
		self.azimuth_absolute_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.azimuth_absolute_edit.setText(self.config_result[3].split(':')[1][0:-3])
		self.azimuth_absolute_unit_label = QLabel('°')
		self.azimuth_current_angle = QTextBrowser()
		self.azimuth_current_angle.setMaximumSize(50, 25)
		self.azimuth_current_angle.setAlignment(QtCore.Qt.AlignCenter)
		self.azimuth_current_unit_label = QLabel('°')
		self.pitching_motion_label = QLabel('俯仰')
		self.pitching_relative_edit = QTextEdit()
		self.pitching_relative_edit.setMaximumSize(50, 25)
		self.pitching_relative_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.pitching_relative_edit.setText(self.config_result[4].split(':')[1][0:-3])
		self.pitching_relative_unit_label = QLabel('°')
		self.pitching_absolute_edit = QTextEdit()
		self.pitching_absolute_edit.setMaximumSize(50, 25)
		self.pitching_absolute_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.pitching_absolute_edit.setText(self.config_result[5].split(':')[1][0:-3])
		self.pitching_absolute_unit_label = QLabel('°')
		self.pitching_current_angle = QTextBrowser()
		self.pitching_current_angle.setMaximumSize(50, 25)
		self.pitching_current_angle.setAlignment(QtCore.Qt.AlignCenter)
		self.pitching_current_unit_label = QLabel('°')
		self.azimuth_relative_edit.setEnabled(True)
		self.pitching_relative_edit.setEnabled(True)
		self.azimuth_absolute_edit.setEnabled(False)
		self.pitching_absolute_edit.setEnabled(False)
		self.connect_button = QPushButton('连接')
		self.connect_button.clicked.connect(self.turn_table_status)
		self.find_home_combo = QComboBox()
		self.find_home_combo.addItems(('水平寻零', '俯仰寻零', '全向寻零'))
		self.find_home_button = QPushButton('寻零')
		self.find_home_button.setEnabled(False)
		self.find_home_button.clicked.connect(self.find_home)
		self.confirm_button = QPushButton('确认')
		self.confirm_button.setEnabled(False)
		self.confirm_button.clicked.connect(self.confirm_config)
		self.result_label = QLabel('状态显示')
		self.result_edit = QTextBrowser()
		self.result_edit.setMinimumHeight(300)
		self.layout_init()

	def layout_init(self):
		self.middle1_h_layout = QHBoxLayout()
		self.middle2_h_layout = QHBoxLayout()
		self.down_grid_layout = QGridLayout()
		self.all_v_layout = QVBoxLayout()
		self.middle1_h_layout.addWidget(self.auto_config_button)
		self.middle1_h_layout.addWidget(self.manual_config_button)
		self.group_box_1.setLayout(self.middle1_h_layout)
		self.middle2_h_layout.addWidget(self.relative_motion_button)
		self.middle2_h_layout.addWidget(self.absolute_motion_button)
		self.group_box_2.setLayout(self.middle2_h_layout)
		self.down_grid_layout.addWidget(self.relative_motion_label, 0, 1, 1, 1)
		self.down_grid_layout.addWidget(self.absolute_motion_label, 0, 3, 1, 1)
		self.down_grid_layout.addWidget(self.current_angle_label, 0, 5, 1, 1)
		self.down_grid_layout.addWidget(self.azimuth_motion_label, 1, 0, 1, 1)
		self.down_grid_layout.addWidget(self.azimuth_relative_edit, 1, 1, 1, 1)
		self.down_grid_layout.addWidget(self.azimuth_relative_unit_label, 1, 2, 1, 1)
		self.down_grid_layout.addWidget(self.azimuth_absolute_edit, 1, 3, 1, 1)
		self.down_grid_layout.addWidget(self.azimuth_absolute_unit_label, 1, 4, 1, 1)
		self.down_grid_layout.addWidget(self.azimuth_current_angle, 1, 5, 1, 1)
		self.down_grid_layout.addWidget(self.azimuth_current_unit_label, 1, 6, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_motion_label, 2, 0, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_relative_edit, 2, 1, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_relative_unit_label, 2, 2, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_absolute_edit, 2, 3, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_absolute_unit_label, 2, 4, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_current_angle, 2, 5, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_current_unit_label, 2, 6, 1, 1)
		self.down_grid_layout.addWidget(self.connect_button, 3, 0, 1, 1)
		self.down_grid_layout.addWidget(self.find_home_combo, 3, 1, 1, 2)
		self.down_grid_layout.addWidget(self.find_home_button, 3, 3, 1, 2)
		self.down_grid_layout.addWidget(self.confirm_button, 3, 5, 1, 2)
		self.all_v_layout.addWidget(self.group_box_1)
		self.all_v_layout.addWidget(self.group_box_2)
		self.all_v_layout.addLayout(self.down_grid_layout)
		self.all_v_layout.addWidget(self.result_label)
		self.all_v_layout.addWidget(self.result_edit)
		self.setLayout(self.all_v_layout)

	def turn_table_status(self):
		if self.connect_button.text() == '连接':
			self.turn_table.connect()
			self.find_home_button.setEnabled(True)
			self.confirm_button.setEnabled(True)
			self.connect_button.setText('断开')
		else:
			self.turn_table.disconnect()
			self.find_home_button.setEnabled(False)
			self.confirm_button.setEnabled(False)
			self.connect_button.setText('连接')

	def find_home(self):
		if self.find_home_combo.currentText() == '水平寻零':
			self.turn_table.s_home(2)
			self.current_angle_azimuth = CurrentAngleAzimuth()
			self.current_angle_pitching = CurrentAnglePitching()
			self.current_angle_azimuth.start()
			self.current_angle_pitching.start()
			self.current_angle_azimuth.my_signal.connect(self.set_current_angle_azimuth_label)
			self.current_angle_pitching.my_signal.connect(self.set_current_angle_pitching_label)
		elif self.find_home_combo.currentText() == '俯仰寻零':
			self.turn_table.s_home(1)
			self.current_angle_azimuth = CurrentAngleAzimuth()
			self.current_angle_pitching = CurrentAnglePitching()
			self.current_angle_azimuth.start()
			self.current_angle_pitching.start()
			self.current_angle_azimuth.my_signal.connect(self.set_current_angle_azimuth_label)
			self.current_angle_pitching.my_signal.connect(self.set_current_angle_pitching_label)
		else:
			self.turn_table.s_home(1)
			self.turn_table.s_home(2)
			self.current_angle_azimuth = CurrentAngleAzimuth()
			self.current_angle_pitching = CurrentAnglePitching()
			self.current_angle_azimuth.start()
			self.current_angle_pitching.start()
			self.current_angle_azimuth.my_signal.connect(self.set_current_angle_azimuth_label)
			self.current_angle_pitching.my_signal.connect(self.set_current_angle_pitching_label)

	def mode_select(self):
		if self.manual_config_button.isChecked():
			if self.relative_motion_button.isChecked():
				self.azimuth_relative_edit.setEnabled(True)
				self.pitching_relative_edit.setEnabled(True)
				self.azimuth_absolute_edit.setEnabled(False)
				self.pitching_absolute_edit.setEnabled(False)
			else:
				self.azimuth_relative_edit.setEnabled(False)
				self.pitching_relative_edit.setEnabled(False)
				self.azimuth_absolute_edit.setEnabled(True)
				self.pitching_absolute_edit.setEnabled(True)
		else:
			self.azimuth_relative_edit.setEnabled(False)
			self.pitching_relative_edit.setEnabled(False)
			self.azimuth_absolute_edit.setEnabled(False)
			self.pitching_absolute_edit.setEnabled(False)

	def confirm_config(self):
		file = open('./config/TurnTable.txt', 'w+')
		if self.manual_config_button.isChecked():
			config_mode = '手动设置'
			self.manual_motion()
		else:
			config_mode = '自动设置'
		if self.relative_motion_button.isChecked():
			motion_mode = '相对移动'
		else:
			motion_mode = '绝对移动'
		file.write('设置控制方式:%s\n'
		           '设置移动方式:%s\n'
		           '设置方位相对移动角度:%s°\n'
		           '设置方位绝对移动角度:%s°\n'
		           '设置俯仰相对移动角度:%s°\n'
		           '设置俯仰绝对移动角度:%s°\n' % (
			           config_mode,
			           motion_mode,
			           self.azimuth_relative_edit.toPlainText(),
			           self.azimuth_absolute_edit.toPlainText(),
			           self.pitching_relative_edit.toPlainText(),
			           self.pitching_absolute_edit.toPlainText()))
		# self.result_edit.setText(self.result_edit.toPlainText() + '完成设置通道：' + self.power_supply.return_status_chan() + 'V ' + time.strftime('%H:%M:%S') + '\n')
		# self.result_edit.setText(self.result_edit.toPlainText() + '完成设置电压：' + self.power_supply.return_status_volt() + 'V ' + time.strftime('%H:%M:%S') + '\n')
		# self.result_edit.setText(self.result_edit.toPlainText() + '完成设置电流：' + self.power_supply.return_status_curr() + 'V ' + time.strftime('%H:%M:%S') + '\n')

	def manual_motion(self):
		if self.relative_motion_button.isChecked():
			self.turn_table.move_to_position(2, float(self.azimuth_relative_edit.toPlainText()), 1, False)
			self.turn_table.move_to_position(1, float(self.pitching_relative_edit.toPlainText()), 1, False)
			self.current_angle_azimuth = CurrentAngleAzimuth()
			self.current_angle_pitching = CurrentAnglePitching()
			self.current_angle_azimuth.start()
			self.current_angle_pitching.start()
			self.current_angle_azimuth.my_signal.connect(self.set_current_angle_azimuth_label)
			self.current_angle_pitching.my_signal.connect(self.set_current_angle_pitching_label)
		else:
			self.turn_table.move_to_position(2, float(self.azimuth_absolute_edit.toPlainText()), 1, True)
			self.turn_table.move_to_position(1, float(self.pitching_absolute_edit.toPlainText()), 1, True)
			self.current_angle_azimuth = CurrentAngleAzimuth()
			self.current_angle_pitching = CurrentAnglePitching()
			self.current_angle_azimuth.start()
			self.current_angle_pitching.start()
			self.current_angle_azimuth.my_signal.connect(self.set_current_angle_azimuth_label)
			self.current_angle_pitching.my_signal.connect(self.set_current_angle_pitching_label)

	def set_current_angle_azimuth_label(self, num):
		self.azimuth_current_angle.setText(num)

	def set_current_angle_pitching_label(self, num):
		self.pitching_current_angle.setText(num)


class CurrentAngleAzimuth(QThread):
	my_signal = pyqtSignal(str)

	def __init__(self):
		super(CurrentAngleAzimuth, self).__init__()

	def run(self):
		self.turn_table = TurnTable()
		self.turn_table.connect()
		time.sleep(2)
		while True:
			self.my_signal.emit(str(round(self.turn_table.get_position(2), 2)))
			self.sleep(1)


class CurrentAnglePitching(QThread):
	my_signal = pyqtSignal(str)

	def __init__(self):
		super(CurrentAnglePitching, self).__init__()

	def run(self):
		self.turn_table = TurnTable()
		self.turn_table.connect()
		time.sleep(2)
		while True:
			self.my_signal.emit(str(round(self.turn_table.get_position(1), 2)))
			self.sleep(1)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	radar_test = RadarTestMain()
	radar_test.show()
	sys.exit(app.exec())
