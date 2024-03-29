from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import *
import sys
import pyqtgraph as pg
from ThreadMission import *
import time
import array
from MachineClass import *


# 主界面
class RadarTestMain(QMainWindow):
	def __init__(self):
		super(RadarTestMain, self).__init__()
		self.init_ui()

	def init_ui(self):
		# self.resize(1100, 700)
		self.setWindowTitle("毫米波雷达自动化测试系统")
		self.data = array.array('i')
		self.move_center()
		self.menu_init()
		self.status_bar_init()
		self.tab_menu_init()

	def move_center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def menu_init(self):
		# 菜单总览
		self.menubar = self.menuBar()
		file_menu = self.menubar.addMenu("文件")
		mission_menu = self.menubar.addMenu("任务")
		# view_menu = menubar.addMenu("视图")
		config_menu = self.menubar.addMenu("配置")
		# analysis_menu = menubar.addMenu("分析")
		self_test_menu = self.menubar.addMenu("自检")
		tool_menu = self.menubar.addMenu("工具")
		# 文件菜单
		# 打开
		open_act = QAction("打开", self)
		open_act.setShortcut('Ctrl+O')
		open_act.triggered.connect(lambda: QFileDialog.getOpenFileName(self, '打开文件', '/home'))
		file_menu.addAction(open_act)
		# 保存
		save_act = QAction("保存", self)
		save_act.setShortcut('Ctrl+S')
		save_act.triggered.connect(lambda: QFileDialog.getSaveFileName(self, '保存文件', '/home'))
		file_menu.addAction(save_act)
		# 退出
		exit_act = QAction("退出", self)
		exit_act.setShortcut("Ctrl+Q")
		exit_act.triggered.connect(qApp.quit)
		file_menu.addAction(exit_act)
		# 任务菜单
		# 新建
		new_mission_act = QAction('新建', self)
		mission_menu.addAction(new_mission_act)
		self.add_mission = AddMission()
		new_mission_act.triggered.connect(self.add_mission.show)
		# 修改
		modify_mission_act = QAction('修改', self)
		mission_menu.addAction(modify_mission_act)
		self.modify_mission = ModifyMission()
		modify_mission_act.triggered.connect(self.modify_mission.show)
		# 配置菜单
		# 电源
		power_supply_act = QAction('电源', self)
		self.power_supply = PowerSupplyConfig()
		power_supply_act.triggered.connect(self.power_supply.show)
		config_menu.addAction(power_supply_act)
		# 频谱仪
		frequency_analysis_act = QAction('频谱仪', self)
		config_menu.addAction(frequency_analysis_act)
		# 信号源
		signal_source_act = QAction('信号源', self)
		config_menu.addAction(signal_source_act)
		# 示波器
		oscilloscope_act = QAction('示波器', self)
		config_menu.addAction(oscilloscope_act)
		# 目标模拟器
		target_simulate_act = QAction('目标模拟器', self)
		config_menu.addAction(target_simulate_act)
		# 转台
		turn_table_act = QAction('转台', self)
		config_menu.addAction(turn_table_act)
		self.turn_table_config = TurnTableConfig()
		turn_table_act.triggered.connect(self.turn_table_config.show)
		# 自检菜单
		radar_connection_act = QAction('连接雷达', self)
		self_test_menu.addAction(radar_connection_act)
		radar_connection_act.triggered.connect(self.get_radar_message)
		# 工具菜单
		# 串口调试工具
		com_act = QAction("串口调试", self)
		# com_act.triggered.connect()
		tool_menu.addAction(com_act)
		# 网口调试工具
		net_act = QAction("网口调试", self)
		# net_act.triggered.connect()
		tool_menu.addAction(net_act)

	def tab_menu_init(self):
		self.tab_widget = QTabWidget(self)
		self.tab1_central_widget = QWidget(self.tab_widget)
		self.tab2_central_widget = QWidget(self.tab_widget)
		self.tab3_central_widget = QWidget(self.tab_widget)
		self.tab_widget.addTab(self.tab1_central_widget, "射频性能测试")
		self.tab_widget.addTab(self.tab2_central_widget, "探测性能测试")
		self.tab_widget.addTab(self.tab3_central_widget, "天线性能测试")
		self.tab_widget.setCurrentIndex(1)
		self.tab_widget.setTabPosition(QTabWidget.North)
		self.tab_widget.setTabShape(QTabWidget.Triangular)
		self.setCentralWidget(self.tab_widget)
		# 设置选中为红色，设置字体及大小
		self.tab_widget.setStyleSheet("QTabBar::tab:selected{color:red;background-color:rbg(200,200,255);} ")
		self.tab_widget.setFont(QFont('KaiTi', 12))
		self.tab1_ui()
		self.tab2_ui()
		self.tab3_ui()

	def status_bar_init(self):
		self.statusBar().showMessage('ready!')

	def tab1_ui(self):
		pass

	def tab1_layout_init(self):
		pass

	def tab2_ui(self):
		# 基本信息
		# 任务信息栏
		self.frame_1 = QFrame(self.tab2_central_widget)
		self.frame_1.setFrameShape(QFrame.StyledPanel)
		# 项目栏
		self.frame_2 = QFrame(self.tab2_central_widget)
		self.frame_2.setFrameShape(QFrame.StyledPanel)
		# self.frame_2.setMaximumWidth(300)
		# 状态栏
		self.frame_3 = QFrame(self.tab2_central_widget)
		self.frame_3.setFrameShape(QFrame.StyledPanel)
		# 目标信息栏
		self.frame_4 = QFrame(self.tab2_central_widget)
		self.frame_4.setFrameShape(QFrame.StyledPanel)
		# self.frame_4.setMaximumWidth(300)
		# 各控件信息
		# 任务信息栏
		self.tab2_sample_number_label = QLabel()
		self.tab2_sample_number_label.setText('样品编号:')
		# self.tab2_sample_number_label.setBaseSizeeze(70,40)
		self.tab2_sample_number_browser = QTextBrowser()
		self.tab2_sample_number_browser.setText('00001')
		self.tab2_sample_number_browser.setAlignment(QtCore.Qt.AlignCenter)
		# self.tab2_sample_number_browser.setBaseSize(70,40)
		self.tab2_tester_name_label = QLabel()
		self.tab2_tester_name_label.setText('测试人员:')
		# self.tab2_tester_name_label.setMinimumSize(50, 20)
		self.tab2_tester_name_browser = QTextBrowser()
		self.tab2_tester_name_browser.setText('薛岩')
		self.tab2_tester_name_browser.setAlignment(QtCore.Qt.AlignCenter)
		# self.tab2_tester_name_browser.setMinimumSize(70, 20)
		self.tab2_supervisor_name_label = QLabel()
		self.tab2_supervisor_name_label.setText('复核/监督人员:')
		# self.tab2_supervisor_name_label.setMinimumSize(100, 20)
		self.tab2_supervisor_name_combo = QComboBox()
		# self.tab2_supervisor_name_combo.setFixedSize(70, 20)
		self.tab2_supervisor_name_combo.addItem('刘力')
		self.tab2_supervisor_name_combo.addItem('申亚飞')
		self.tab2_supervisor_name_combo.addItem('裴毓')
		self.tab2_supervisor_name_combo.addItem('张晓蕾')
		self.tab2_supervisor_name_combo.addItem('薛岩')
		self.tab2_test_data_label = QLabel()
		self.tab2_test_data_label.setText('试验日期:')
		# self.tab2_test_data_label.setFixedSize(70, 20)
		self.tab2_test_data_edit = QDateEdit()
		self.tab2_test_data_edit.setAlignment(QtCore.Qt.AlignCenter)
		# self.tab2_test_data_edit.setFixedSize(100, 20)
		self.tab2_test_data_edit.setCalendarPopup(True)
		self.tab2_test_data_edit.setDate(QtCore.QDate.currentDate())
		# 仪表状态栏
		# self.tab2_status_turntable_button = QPushButton('连接转台')
		self.tab2_status_turntable_button = QLabel()
		self.tab2_status_turntable_button.setFixedSize(20, 20)
		self.tab2_status_turntable_button.setScaledContents(True)
		self.tab2_status_turntable_button.setPixmap(QPixmap('./image/wifi_off.png'))
		# self.tab2_status_turntable_button.clicked.connect(self.get_turn_table_status)
		self.tab2_status_power_supply_button = QPushButton('连接电源')
		# self.tab2_status_power_supply_button.setFixedSize(100, 20)
		self.tab2_status_power_supply_button.setIcon(QIcon('./image/wifi_off.png'))
		self.tab2_status_target_simulate_button = QPushButton('连接目标模拟器')
		# self.tab2_status_target_simulate_button.setFixedSize(100, 20)
		self.tab2_status_target_simulate_button.setIcon(QIcon('./image/wifi_off.png'))
		self.tab2_status_radar_can_button = QPushButton('连接雷达CAN通信')
		# self.tab2_status_radar_can_button.setFixedSize(100, 20)
		self.tab2_status_radar_can_button.setIcon(QIcon('./image/wifi_off.png'))
		# 项目栏
		self.tab2_horizontal_power_box = QCheckBox('水平探测威力')
		self.tab2_vertical_power_box = QCheckBox('垂直探测威力')
		self.tab2_distance_resolution_box = QCheckBox('距离分辨率')
		self.tab2_distance_distinction_box = QCheckBox('距离区分度')
		self.tab2_horizontal_angular_range_box = QCheckBox('水平角度范围')
		self.tab2_vertical_angular_range_box = QCheckBox('垂直角度范围')
		self.tab2_angular_resolution_box = QCheckBox('角度分辨率')
		self.tab2_angular_distinction_box = QCheckBox('角度区分度')
		self.tab2_speed_range_box = QCheckBox('速度范围')
		self.tab2_speed_resolution_box = QCheckBox('速度分辨率')
		self.tab2_speed_distinction_box = QCheckBox('速度区分度')
		self.tab2_test_start_button = QPushButton('开始测试')
		self.tab2_test_pause_button = QPushButton('暂停测试')
		self.tab2_test_stop_button = QPushButton('终止测试')
		# 水平威力范围设置按钮功能定义
		self.tab2_horizontal_power_config_button = QPushButton('设置')
		self.tab2_horizontal_power_config_button.setEnabled(False)
		self.horizontal_power_config_menu_window = HorizontalPowerMenu()
		self.tab2_horizontal_power_config_button.clicked.connect(
			self.horizontal_power_config_menu_window.show)
		# 水平威力范围按钮显示，勾取后可以设置
		self.tab2_horizontal_power_box.stateChanged.connect(
			lambda:
			self.tab2_horizontal_power_config_button.setEnabled(True)
			if self.tab2_horizontal_power_box.checkState() == 2
			else self.tab2_horizontal_power_config_button.setEnabled(False))
		# 垂直威力范围设置按钮功能定义
		self.tab2_vertical_power_config_button = QPushButton('设置')
		self.tab2_vertical_power_config_button.setEnabled(False)
		self.vertical_power_config_menu_window = VerticalPowerMenu()
		self.tab2_vertical_power_config_button.clicked.connect(
			self.vertical_power_config_menu_window.show)
		# 垂直威力范围按钮显示，勾取后可以设置
		self.tab2_vertical_power_box.stateChanged.connect(
			lambda:
			self.tab2_vertical_power_config_button.setEnabled(True)
			if self.tab2_vertical_power_box.checkState() == 2
			else self.tab2_vertical_power_config_button.setEnabled(False))
		# 距离分辨率设置按钮功能定义
		self.tab2_distance_resolution_config_button = QPushButton('设置')
		self.tab2_distance_resolution_config_button.setEnabled(False)
		self.distance_resolution_config_menu_window = DistanceResolution()
		self.tab2_distance_resolution_config_button.clicked.connect(
			self.distance_resolution_config_menu_window.show)
		# 距离分辨率按钮显示，勾取后可以设置
		self.tab2_distance_resolution_box.stateChanged.connect(
			lambda:
			self.tab2_distance_resolution_config_button.setEnabled(True)
			if self.tab2_distance_resolution_box.checkState() == 2
			else self.tab2_distance_resolution_config_button.setEnabled(False))
		# 距离区分度设置按钮功能定义
		self.tab2_distance_distinction_config_button = QPushButton('设置')
		self.tab2_distance_distinction_config_button.setEnabled(False)
		self.distance_distinction_config_menu_window = DistanceDistinction()
		self.tab2_distance_distinction_config_button.clicked.connect(
			self.distance_distinction_config_menu_window.show)
		# 距离区分度按钮显示，勾取后可以设置
		self.tab2_distance_distinction_box.stateChanged.connect(
			lambda:
			self.tab2_distance_distinction_config_button.setEnabled(True)
			if self.tab2_distance_distinction_box.checkState() == 2
			else self.tab2_distance_distinction_config_button.setEnabled(False))
		# 水平角度范围设置按钮功能定义
		self.tab2_horizontal_angular_range_config_button = QPushButton('设置')
		self.tab2_horizontal_angular_range_config_button.setEnabled(False)
		self.horizontal_angular_range_config_menu_window = HorizontalAngularRange()
		self.tab2_horizontal_angular_range_config_button.clicked.connect(
			self.horizontal_angular_range_config_menu_window.show)
		# 水平角度范围按钮显示，勾取后可以设置
		self.tab2_horizontal_angular_range_box.stateChanged.connect(
			lambda:
			self.tab2_horizontal_angular_range_config_button.setEnabled(True)
			if self.tab2_horizontal_angular_range_box.checkState() == 2
			else self.tab2_horizontal_angular_range_config_button.setEnabled(False))
		# 垂直角度范围设置按钮功能定义
		self.tab2_vertical_angular_range_config_button = QPushButton('设置')
		self.tab2_vertical_angular_range_config_button.setEnabled(False)
		self.vertical_angular_range_config_menu_window = VerticalAngularRange()
		self.tab2_vertical_angular_range_config_button.clicked.connect(
			self.vertical_angular_range_config_menu_window.show)
		# 垂直角度范围按钮显示，勾取后可以设置
		self.tab2_vertical_angular_range_box.stateChanged.connect(
			lambda:
			self.tab2_vertical_angular_range_config_button.setEnabled(True)
			if self.tab2_vertical_angular_range_box.checkState() == 2
			else self.tab2_vertical_angular_range_config_button.setEnabled(False))
		# 角度分辨率设置按钮功能定义
		self.tab2_angular_resolution_config_button = QPushButton('设置')
		self.tab2_angular_resolution_config_button.setEnabled(False)
		self.angular_resolution_config_menu_window = AngularResolution()
		self.tab2_angular_resolution_config_button.clicked.connect(
			self.angular_resolution_config_menu_window.show)
		# 角度分辨率按钮显示，勾取后可以设置
		self.tab2_angular_resolution_box.stateChanged.connect(
			lambda:
			self.tab2_angular_resolution_config_button.setEnabled(True)
			if self.tab2_angular_resolution_box.checkState() == 2
			else self.tab2_angular_resolution_config_button.setEnabled(False))
		# 角度区分度设置按钮功能定义
		self.tab2_angular_distinction_config_button = QPushButton('设置')
		self.tab2_angular_distinction_config_button.setEnabled(False)
		self.angular_distinction_config_menu_window = AngularDistinction()
		self.tab2_angular_distinction_config_button.clicked.connect(
			self.angular_distinction_config_menu_window.show)
		# 角度区分度按钮显示，勾取后可以设置
		self.tab2_angular_distinction_box.stateChanged.connect(
			lambda:
			self.tab2_angular_distinction_config_button.setEnabled(True)
			if self.tab2_angular_distinction_box.checkState() == 2
			else self.tab2_angular_distinction_config_button.setEnabled(False))
		# 速度范围设置按钮功能定义
		self.tab2_speed_range_config_button = QPushButton('设置')
		self.tab2_speed_range_config_button.setEnabled(False)
		self.speed_range_config_menu_window = SpeedRange()
		self.tab2_speed_range_config_button.clicked.connect(
			self.speed_range_config_menu_window.show)
		# 速度范围按钮显示，勾取后可以设置
		self.tab2_speed_range_box.stateChanged.connect(
			lambda:
			self.tab2_speed_range_config_button.setEnabled(True)
			if self.tab2_speed_range_box.checkState() == 2
			else self.tab2_speed_range_config_button.setEnabled(False))
		# 速度分辨率设置按钮功能定义
		self.tab2_speed_resolution_config_button = QPushButton('设置')
		self.tab2_speed_resolution_config_button.setEnabled(False)
		self.speed_resolution_config_menu_window = SpeedResolution()
		self.tab2_speed_resolution_config_button.clicked.connect(
			self.speed_resolution_config_menu_window.show)
		# 速度分辨率按钮显示，勾取后可以设置
		self.tab2_speed_resolution_box.stateChanged.connect(
			lambda:
			self.tab2_speed_resolution_config_button.setEnabled(True)
			if self.tab2_speed_resolution_box.checkState() == 2
			else self.tab2_speed_resolution_config_button.setEnabled(False))
		# 速度区分度设置按钮功能定义
		self.tab2_speed_distinction_config_button = QPushButton('设置')
		self.tab2_speed_distinction_config_button.setEnabled(False)
		self.speed_distinction_config_menu_window = SpeedDistinction()
		self.tab2_speed_distinction_config_button.clicked.connect(
			self.speed_distinction_config_menu_window.show)
		# 速度区分度按钮显示，勾取后可以设置
		self.tab2_speed_distinction_box.stateChanged.connect(
			lambda:
			self.tab2_speed_distinction_config_button.setEnabled(True)
			if self.tab2_speed_distinction_box.checkState() == 2
			else self.tab2_speed_distinction_config_button.setEnabled(False))
		# 状态栏
		self.tab2_status_test_label = QLabel('测试状态')
		self.tab2_status_test_edit = QTextBrowser()
		self.tab2_status_test_edit.setStyleSheet(
			'background-color:white;font-size:12px')
		# 状态栏始终显示底部
		self.tab2_status_test_edit.ensureCursorVisible()  # 游标可用
		cursor = self.tab2_status_test_edit.textCursor()  # 设置游标
		pos = len(self.tab2_status_test_edit.toPlainText())  # 获取文本尾部的位置
		cursor.setPosition(pos)  # 游标位置设置为尾部
		self.tab2_status_test_edit.setTextCursor(cursor)  # 滚动到游标位置
		# 试验结果栏
		self.tab2_result_test_label = QLabel('试验结果')
		self.tab2_result_test_edit = QTextBrowser()
		# 目标信息栏
		self.tab2_realtime_plot = pg.PlotWidget()
		self.tab2_realtime_plot.showGrid(x=True, y=True)
		self.tab2_realtime_plot.setXRange(-5, 5)
		self.tab2_realtime_plot.setYRange(0, 40)
		self.tab2_realtime_plot_ready = self.tab2_realtime_plot.plot(
			np.random.normal(size=1), np.random.normal(size=1))
		self.tab2_realtime_table = QTableWidget()
		self.tab2_realtime_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.tab2_realtime_table.setColumnCount(6)
		self.tab2_realtime_table.setRowCount(20)
		self.tab2_realtime_table.setHorizontalHeaderLabels(
			['ID', '垂直距离', '水平距离', '垂直速度', '水平速度', '目标RCS'])
		# 位置初始化
		self.tab2_layout_init()

	# 性能测试布局
	def tab2_layout_init(self):
		# ---底层界面布局---
		# 任务信息栏布局
		self.tab2_1_0_h_layout = QHBoxLayout()
		self.tab2_1_0_h_layout.addWidget(self.tab2_sample_number_label)
		self.tab2_1_0_h_layout.addWidget(self.tab2_sample_number_browser)
		self.tab2_1_0_h_layout.addWidget(self.tab2_tester_name_label)
		self.tab2_1_0_h_layout.addWidget(self.tab2_tester_name_browser)
		self.tab2_1_0_h_layout.addWidget(self.tab2_supervisor_name_label)
		self.tab2_1_0_h_layout.addWidget(self.tab2_supervisor_name_combo)
		self.tab2_1_0_h_layout.addWidget(self.tab2_test_data_label)
		self.tab2_1_0_h_layout.addWidget(self.tab2_test_data_edit)
		# 仪表状态栏布局
		self.tab_1_1_h_layout = QHBoxLayout()
		self.tab_1_1_h_layout.addWidget(self.tab2_status_turntable_button)
		self.tab_1_1_h_layout.addWidget(self.tab2_status_power_supply_button)
		self.tab_1_1_h_layout.addWidget(self.tab2_status_target_simulate_button)
		self.tab_1_1_h_layout.addWidget(self.tab2_status_radar_can_button)
		# 任务栏+ 仪表状态栏布局
		self.tab2_1_h_layout = QVBoxLayout()
		self.tab2_1_h_layout.addLayout(self.tab2_1_0_h_layout)
		self.tab2_1_h_layout.addLayout(self.tab_1_1_h_layout)
		self.frame_1.setLayout(self.tab2_1_h_layout)
		# 项目栏布局
		self.tab2_2_grid_layout = QGridLayout()
		self.tab2_2_grid_layout.addWidget(self.tab2_horizontal_power_box, 0, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_horizontal_power_config_button, 0, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_vertical_power_box, 1, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_vertical_power_config_button, 1, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_distance_resolution_box, 2, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_distance_resolution_config_button, 2, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_distance_distinction_box, 3, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_distance_distinction_config_button, 3, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_horizontal_angular_range_box, 4, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_horizontal_angular_range_config_button, 4, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_vertical_angular_range_box, 5, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_vertical_angular_range_config_button, 5, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_angular_resolution_box, 6, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_angular_resolution_config_button, 6, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_angular_distinction_box, 7, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_angular_distinction_config_button, 7, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_speed_range_box, 8, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_speed_range_config_button, 8, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_speed_resolution_box, 9, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_speed_resolution_config_button, 9, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_speed_distinction_box, 10, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_speed_distinction_config_button, 10, 2, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_test_start_button, 11, 0, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_test_pause_button, 11, 1, 1, 1)
		self.tab2_2_grid_layout.addWidget(self.tab2_test_stop_button, 11, 2, 1, 1)
		self.frame_2.setLayout(self.tab2_2_grid_layout)
		# 状态栏布局
		self.tab2_3_v_layout = QVBoxLayout()
		self.tab2_3_v_layout.addWidget(self.tab2_status_test_label)
		self.tab2_3_v_layout.addWidget(self.tab2_status_test_edit)
		self.tab2_3_v_layout.addWidget(self.tab2_result_test_label)
		self.tab2_3_v_layout.addWidget(self.tab2_result_test_edit)
		self.tab2_3_v_layout.addWidget(self.tab2_realtime_table)
		self.frame_3.setLayout(self.tab2_3_v_layout)
		self.frame_3.setMinimumWidth(400)
		# 目标信息栏布局
		self.tab2_4_v_layout = QVBoxLayout()
		self.tab2_4_v_layout.addWidget(self.tab2_realtime_plot)
		self.frame_4.setLayout(self.tab2_4_v_layout)
		# 项目栏+状态栏布局
		self.tab2_1_h_splitter = QSplitter(Qt.Horizontal)
		self.tab2_1_h_splitter.addWidget(self.frame_2)
		self.tab2_1_h_splitter.addWidget(self.frame_3)
		# 任务信息栏+项目栏+状态栏布局
		self.tab2_2_v_splitter = QSplitter(Qt.Vertical)
		self.tab2_2_v_splitter.addWidget(self.frame_1)
		self.tab2_2_v_splitter.addWidget(self.tab2_1_h_splitter)
		# 任务信息栏+项目栏+状态栏+目标信息栏布局
		self.tab2_3_h_splitter = QSplitter(Qt.Horizontal)
		self.tab2_3_h_splitter.addWidget(self.tab2_2_v_splitter)
		self.tab2_3_h_splitter.addWidget(self.frame_4)
		# 最终布局
		self.tab2_5_v_layout = QVBoxLayout()
		self.tab2_5_v_layout.addWidget(self.tab2_3_h_splitter)
		self.tab2_central_widget.setLayout(self.tab2_5_v_layout)

	def get_turn_table_status(self):
		if self.tab2_status_turntable_button.text() == '连接转台':
			self.tab2_status_turntable_button.setIcon(QIcon('./image/wifi_on.png'))
			self.tab2_status_turntable_button.setText('断开转台连接')
			self.turn_table = TurnTable()
			self.turn_table.connect()
			self.turn_table_status = TurnTableStatus(self.turn_table)
			self.turn_table_status.start()
			self.turn_table_status.my_signal.connect(
				self.display_turn_table_status)
		else:
			self.tab2_status_turntable_button.setText('连接转台')
			self.tab2_status_turntable_button.setIcon(QIcon('./image/wifi_off.png'))

	def display_turn_table_status(self, angle):
		print(angle[0])
		print(angle[1])
		pass

	# 自检菜单选项
	# 雷达信号接收
	def get_radar_message(self):
		# 初始化雷达目标信息
		self.message = []
		self.get_message = GetMessage()
		self.get_message.start()
		self.get_message.my_signal.connect(self.set_message)
		self.timer = pg.QtCore.QTimer()
		self.timer.timeout.connect(lambda: self.paint_message(self.message))
		self.timer.start(500)

	# 获取目标初始信息
	def set_message(self, message):
		self.message = message

	# 画面、表格显示目标信息
	def paint_message(self, message):
		new_message = np.array(message)
		self.tab2_realtime_table.clear()
		self.tab2_realtime_table.setHorizontalHeaderLabels(
			['ID', '垂直距离', '水平距离', '垂直速度', '水平速度', '目标RCS'])
		if len(new_message) > 0:
			self.tab2_realtime_plot_ready.setData(new_message[:, 2], new_message[:, 1], pen=None, symbol='o')
			# print(new_message)
			for i in range(len(new_message)):
				for j in range(6):
					self.tab2_realtime_table.setItem(i, j, QTableWidgetItem(str(new_message[i, j])))
					item_ij = self.tab2_realtime_table.item(i, j)
					item_ij.setTextAlignment(Qt.AlignCenter)

	# 目标模拟器主界面设置按钮跳转
	def target_simulate_config(self):
		self.target_simulate = ARTS()

	# self.target_simulate.show()

	def tab3_ui(self):
		pass


# 水平威力范围详细菜单
class HorizontalPowerMenu(QWidget):
	def __init__(self):
		super(HorizontalPowerMenu, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('水平威力范围设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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
		# 布局初始化
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

	def showEvent(self, event):
		# 界面数据初始化
		try:
			file = open('./config/HorizontalPowerTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-3])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取水平威力范围配置文件失败!')
		else:
			file.close()
		event.accept()

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
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 垂直威力范围详细菜单
class VerticalPowerMenu(QWidget):
	def __init__(self):
		super(VerticalPowerMenu, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('垂直威力范围设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/VerticalPowerTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-3])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取垂直威力范围配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/VerticalPowerTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 距离辨分率详细菜单
class DistanceResolution(QWidget):
	def __init__(self):
		super(DistanceResolution, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('距离分辨率设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/DistanceResolutionTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取距离辨分率配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/DistanceResolutionTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 距离区分度详细菜单
class DistanceDistinction(QWidget):
	def __init__(self):
		super(DistanceDistinction, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('距离区分度设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/DistanceResolutionTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取距离区分度配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/DistanceDistinctionTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 水平角度范围详细菜单
class HorizontalAngularRange(QWidget):
	def __init__(self):
		super(HorizontalAngularRange, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('水平角度范围设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/DistanceResolutionTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取水平角度范围配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/HorizontalAngularRangeTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 垂直角度范围详细菜单
class VerticalAngularRange(QWidget):
	def __init__(self):
		super(VerticalAngularRange, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('垂直角度范围设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/VerticalAngularRangeTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取垂直角度范围配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/VerticalAngularRangeTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 角度分辨率详细菜单
class AngularResolution(QWidget):
	def __init__(self):
		super(AngularResolution, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('角度分辨率设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/AngularResolutionTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取角度分辨率配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/AngularResolutionTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 角度区分度详细菜单
class AngularDistinction(QWidget):
	def __init__(self):
		super(AngularDistinction, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('角度区分度设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/AngularDistinctionTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取角度区分度配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/AngularDistinctionTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 速度范围详细菜单
class SpeedRange(QWidget):
	def __init__(self):
		super(SpeedRange, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('速度范围设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/SpeedRangeTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取速度范围配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/SpeedRangeTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 速度分辨率详细菜单
class SpeedResolution(QWidget):
	def __init__(self):
		super(SpeedResolution, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('速度分辨率设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/SpeedResolutionTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取速度分辨率配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/SpeedResolutionTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 速度区分度详细菜单
class SpeedDistinction(QWidget):
	def __init__(self):
		super(SpeedDistinction, self).__init__()
		self.resize(200, 200)
		self.setWindowTitle('速度区分度设置')
		self.target_rcs_label = QLabel('目标RCS数值')
		self.target_rcs_edit = QTextEdit()
		self.target_rcs_edit.setMaximumSize(50, 25)
		self.target_rcs_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.target_rcs_unit_label = QLabel('dBsm')
		self.min_range_label = QLabel('最小测试距离')
		self.min_range_edit = QTextEdit()
		self.min_range_edit.setMaximumSize(50, 25)
		self.min_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_range_unit_label = QLabel('m')
		self.max_range_label = QLabel('最大测试距离')
		self.max_range_edit = QTextEdit()
		self.max_range_edit.setMaximumSize(50, 25)
		self.max_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_range_unit_label = QLabel('m')
		self.min_angle_label = QLabel('最小测试角度')
		self.min_angle_edit = QTextEdit()
		self.min_angle_edit.setMaximumSize(50, 25)
		self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.min_angle_unit_label = QLabel('°')
		self.max_angle_label = QLabel('最大测试角度')
		self.max_angle_edit = QTextEdit()
		self.max_angle_edit.setMaximumSize(50, 25)
		self.max_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.max_angle_unit_label = QLabel('°')
		self.step_range_label = QLabel('距离步进')
		self.step_range_edit = QTextEdit()
		self.step_range_edit.setMaximumSize(50, 25)
		self.step_range_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_range_unit_label = QLabel('m')
		self.step_angle_label = QLabel('角度步进')
		self.step_angle_edit = QTextEdit()
		self.step_angle_edit.setMaximumSize(50, 25)
		self.step_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.step_angle_unit_label = QLabel('°')
		self.dwell_time_label = QLabel('驻留时间')
		self.dwell_time_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/SpeedDistinctionTest.txt', encoding='unicode_escape')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.target_rcs_edit.setText(self.edit_result[0].split(':')[1][0:-5])
				self.min_range_edit.setText(self.edit_result[1].split(':')[1][0:-2])
				self.max_range_edit.setText(self.edit_result[2].split(':')[1][0:-2])
				self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-3])
				self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-3])
				self.step_range_edit.setText(self.edit_result[5].split(':')[1][0:-2])
				self.step_angle_edit.setText(self.edit_result[6].split(':')[1][0:-2])
				self.dwell_time_edit.setText(self.edit_result[7].split(':')[1][0:-2])
		except IOError:
			print('读取速度区分度配置文件失败!')
		else:
			file.close()
		event.accept()

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
		file = open('./config/SpeedDistinctionTest.txt', 'w+')
		file.write('目标RCS设置为:%sdBsm\n'
		           '最小测试距离设置为:%sm\n'
		           '最大测试距离设置为:%sm\n'
		           '最小测试角度设置为:%s°\n'
		           '最大测试角度设置为:%s°\n'
		           '步进距离设置为:%sm\n'
		           '步进角度设置为:%s°\n'
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
		time.sleep(1)
		self.close()


# 新建任务
class AddMission(QWidget):
	def __init__(self):
		super(AddMission, self).__init__()
		self.setWindowTitle('新建任务信息')
		self.sample_name_button = QPushButton('样品名称：')
		self.sample_name_button.clicked.connect(self.echo_sample_name)
		self.sample_name_text = QTextBrowser()
		self.sample_name_text.setMaximumSize(250, 25)
		self.sample_type_button = QPushButton('型号规格：')
		self.sample_type_button.clicked.connect(self.echo_sample_type)
		self.sample_type_text = QTextBrowser()
		self.sample_type_text.setMaximumSize(250, 25)
		self.sample_number_button = QPushButton('样品编号：')
		self.sample_number_button.clicked.connect(self.echo_sample_number)
		self.sample_number_text = QTextBrowser()
		self.sample_number_text.setMaximumSize(250, 25)
		self.report_number_button = QPushButton('报告编号：')
		self.report_number_button.clicked.connect(self.echo_report_number)
		self.report_number_text = QTextBrowser()
		self.report_number_text.setMaximumSize(250, 25)
		self.request_company_button = QPushButton('委托单位：')
		self.request_company_button.clicked.connect(self.echo_request_company)
		self.request_company_text = QTextBrowser()
		self.request_company_text.setMaximumSize(250, 25)
		self.test_date_button = QPushButton('试验日期：')
		self.test_date_text = QDateEdit()
		self.test_date_text.setMaximumSize(250, 25)
		self.test_date_text.setCalendarPopup(True)
		self.test_date_text.setDate(QtCore.QDate.currentDate())
		self.test_date_text.setAlignment(QtCore.Qt.AlignCenter)
		self.test_basis_button = QPushButton('试验依据：')
		self.test_basis_button.clicked.connect(self.echo_test_basis)
		self.test_basis_text = QTextBrowser()
		self.test_basis_text.setMaximumSize(250, 40)
		self.test_basis_text.setAlignment(QtCore.Qt.AlignCenter)
		self.test_worker_button = QPushButton('测试人员：')
		self.test_worker_button.clicked.connect(self.echo_test_worker)
		self.test_worker_text = QTextBrowser()
		self.test_worker_text.setMaximumSize(250, 25)
		self.supervise_worker_button = QPushButton('监督人员：')
		self.supervise_worker_button.clicked.connect(self.echo_supervise_worker)
		self.supervise_worker_text = QTextBrowser()
		self.supervise_worker_text.setMaximumSize(250, 25)
		self.confirm_button = QPushButton('确认')
		self.confirm_button.clicked.connect(self.confirm_information)
		self.layout_init()

	def layout_init(self):
		self.grid_layout = QGridLayout(self)
		self.grid_layout.addWidget(self.sample_name_button, 0, 0, 1, 1)
		self.grid_layout.addWidget(self.sample_name_text, 0, 1, 1, 1)
		self.grid_layout.addWidget(self.sample_type_button, 1, 0, 1, 1)
		self.grid_layout.addWidget(self.sample_type_text, 1, 1, 1, 1)
		self.grid_layout.addWidget(self.sample_number_button, 2, 0, 1, 1)
		self.grid_layout.addWidget(self.sample_number_text, 2, 1, 1, 1)
		self.grid_layout.addWidget(self.report_number_button, 3, 0, 1, 1)
		self.grid_layout.addWidget(self.report_number_text, 3, 1, 1, 1)
		self.grid_layout.addWidget(self.request_company_button, 4, 0, 1, 1)
		self.grid_layout.addWidget(self.request_company_text, 4, 1, 1, 1)
		self.grid_layout.addWidget(self.test_date_button, 5, 0, 1, 1)
		self.grid_layout.addWidget(self.test_date_text, 5, 1, 1, 1)
		self.grid_layout.addWidget(self.test_basis_button, 6, 0, 1, 1)
		self.grid_layout.addWidget(self.test_basis_text, 6, 1, 1, 1)
		self.grid_layout.addWidget(self.test_worker_button, 7, 0, 1, 1)
		self.grid_layout.addWidget(self.test_worker_text, 7, 1, 1, 1)
		self.grid_layout.addWidget(self.supervise_worker_button, 8, 0, 1, 1)
		self.grid_layout.addWidget(self.supervise_worker_text, 8, 1, 1, 1)
		self.grid_layout.addWidget(self.confirm_button, 9, 1, 1, 1)
		self.setLayout(self.grid_layout)

	def echo_sample_name(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入样品名称：', QLineEdit.Normal)
		self.sample_name_text.setText(value)
		self.sample_name_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_sample_type(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入型号规格：', QLineEdit.Normal)
		self.sample_type_text.setText(value)
		self.sample_type_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_sample_number(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入样品编号：', QLineEdit.Normal)
		self.sample_number_text.setText(value)
		self.sample_number_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_report_number(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入报告编号：', QLineEdit.Normal)
		self.report_number_text.setText(value)
		self.report_number_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_request_company(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入委托单位：', QLineEdit.Normal)
		self.request_company_text.setText(value)
		self.request_company_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_test_basis(self):
		items = ['GB∕T 36654-2018 76GHz车辆无线电设备射频指标技术要求及测试方法',
		         '毫米波雷达上海市地方标准',
		         '毫米波雷达国家标准',
		         '毫米波雷达企业标准']
		value, ok = QInputDialog.getItem(self, '新建任务信息', '请选择试验依据：', items, 1, True)
		self.test_basis_text.setText(value)
		self.test_basis_text.setAlignment(QtCore.Qt.AlignHCenter)

	def echo_test_worker(self):
		items = ['薛岩', '裴毓', '张晓蕾', '刘力']
		value, ok = QInputDialog.getItem(self, '新建任务信息', '请输入测试人员：', items, 1, True)
		self.test_worker_text.setText(value)
		self.test_worker_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_supervise_worker(self):
		items = ['薛岩', '裴毓', '张晓蕾', '刘力']
		value, ok = QInputDialog.getItem(self, '新建任务信息', '请输入监督人员：', items, 1, True)
		self.supervise_worker_text.setText(value)
		self.supervise_worker_text.setAlignment(QtCore.Qt.AlignCenter)

	def confirm_information(self):
		file = open('./config/MissionInformation.txt', 'w+')
		file.write(
			'样品名称:{0}\n'
			'型号规格:{1}\n'
			'样品编号:{2}\n'
			'报告编号:{3}\n'
			'委托单位:{4}\n'
			'试验日期:{5}\n'
			'试验依据:{6}\n'
			'测试人员:{7}\n'
			'监督人员:{8}\n'.format(
				self.sample_name_text.toPlainText(),
				self.sample_type_text.toPlainText(),
				self.sample_number_text.toPlainText(),
				self.report_number_text.toPlainText(),
				self.request_company_text.toPlainText(),
				self.test_date_text.date().toString(Qt.ISODate),
				self.test_basis_text.toPlainText(),
				self.test_worker_text.toPlainText(),
				self.supervise_worker_text.toPlainText()))
	# time.sleep(1)
	# self.close()


# 修改任务
class ModifyMission(QWidget):
	def __init__(self):
		super(ModifyMission, self).__init__()
		self.setWindowTitle('新建任务信息')
		self.sample_name_button = QPushButton('样品名称：')
		self.sample_name_button.clicked.connect(self.echo_sample_name)
		self.sample_name_text = QTextBrowser()
		self.sample_name_text.setMaximumSize(250, 25)
		self.sample_type_button = QPushButton('型号规格：')
		self.sample_type_button.clicked.connect(self.echo_sample_type)
		self.sample_type_text = QTextBrowser()
		self.sample_type_text.setMaximumSize(250, 25)
		self.sample_number_button = QPushButton('样品编号：')
		self.sample_number_button.clicked.connect(self.echo_sample_number)
		self.sample_number_text = QTextBrowser()
		self.sample_number_text.setMaximumSize(250, 25)
		self.report_number_button = QPushButton('报告编号：')
		self.report_number_button.clicked.connect(self.echo_report_number)
		self.report_number_text = QTextBrowser()
		self.report_number_text.setMaximumSize(250, 25)
		self.request_company_button = QPushButton('委托单位：')
		self.request_company_button.clicked.connect(self.echo_request_company)
		self.request_company_text = QTextBrowser()
		self.request_company_text.setMaximumSize(250, 25)
		self.test_date_button = QPushButton('试验日期：')
		self.test_date_text = QDateEdit()
		self.test_date_text.setMaximumSize(250, 25)
		self.test_date_text.setCalendarPopup(True)
		self.test_date_text.setDate(QtCore.QDate.currentDate())
		self.test_date_text.setAlignment(QtCore.Qt.AlignCenter)
		self.test_basis_button = QPushButton('试验依据：')
		self.test_basis_button.clicked.connect(self.echo_test_basis)
		self.test_basis_text = QTextBrowser()
		self.test_basis_text.setMaximumSize(250, 40)
		self.test_basis_text.setAlignment(QtCore.Qt.AlignCenter)
		self.test_worker_button = QPushButton('测试人员：')
		self.test_worker_button.clicked.connect(self.echo_test_worker)
		self.test_worker_text = QTextBrowser()
		self.test_worker_text.setMaximumSize(250, 25)
		self.supervise_worker_button = QPushButton('监督人员：')
		self.supervise_worker_button.clicked.connect(self.echo_supervise_worker)
		self.supervise_worker_text = QTextBrowser()
		self.supervise_worker_text.setMaximumSize(250, 25)
		self.confirm_button = QPushButton('确认')
		self.confirm_button.clicked.connect(self.confirm_information)
		self.layout_init()

	def layout_init(self):
		self.grid_layout = QGridLayout(self)
		self.grid_layout.addWidget(self.sample_name_button, 0, 0, 1, 1)
		self.grid_layout.addWidget(self.sample_name_text, 0, 1, 1, 1)
		self.grid_layout.addWidget(self.sample_type_button, 1, 0, 1, 1)
		self.grid_layout.addWidget(self.sample_type_text, 1, 1, 1, 1)
		self.grid_layout.addWidget(self.sample_number_button, 2, 0, 1, 1)
		self.grid_layout.addWidget(self.sample_number_text, 2, 1, 1, 1)
		self.grid_layout.addWidget(self.report_number_button, 3, 0, 1, 1)
		self.grid_layout.addWidget(self.report_number_text, 3, 1, 1, 1)
		self.grid_layout.addWidget(self.request_company_button, 4, 0, 1, 1)
		self.grid_layout.addWidget(self.request_company_text, 4, 1, 1, 1)
		self.grid_layout.addWidget(self.test_date_button, 5, 0, 1, 1)
		self.grid_layout.addWidget(self.test_date_text, 5, 1, 1, 1)
		self.grid_layout.addWidget(self.test_basis_button, 6, 0, 1, 1)
		self.grid_layout.addWidget(self.test_basis_text, 6, 1, 1, 1)
		self.grid_layout.addWidget(self.test_worker_button, 7, 0, 1, 1)
		self.grid_layout.addWidget(self.test_worker_text, 7, 1, 1, 1)
		self.grid_layout.addWidget(self.supervise_worker_button, 8, 0, 1, 1)
		self.grid_layout.addWidget(self.supervise_worker_text, 8, 1, 1, 1)
		self.grid_layout.addWidget(self.confirm_button, 9, 1, 1, 1)
		self.setLayout(self.grid_layout)

	def showEvent(self, event):
		try:
			file = open('./config/MissionInformation.txt')
			self.edit_result = file.readlines()
			if self.edit_result:
				self.sample_name_text.setText(self.edit_result[0].split(':')[1][0:-1])
				self.sample_name_text.setAlignment(QtCore.Qt.AlignCenter)
				self.sample_type_text.setText(self.edit_result[1].split(':')[1][0:-1])
				self.sample_type_text.setAlignment(QtCore.Qt.AlignCenter)
				self.sample_number_text.setText(self.edit_result[2].split(':')[1][0:-1])
				self.sample_number_text.setAlignment(QtCore.Qt.AlignCenter)
				self.report_number_text.setText(self.edit_result[3].split(':')[1][0:-1])
				self.report_number_text.setAlignment(QtCore.Qt.AlignCenter)
				self.request_company_text.setText(self.edit_result[4].split(':')[1][0:-1])
				self.request_company_text.setAlignment(QtCore.Qt.AlignCenter)
				self.date = self.edit_result[5].split(':')[1][0:-1]
				self.date_year = int(self.date.split('-')[0])
				self.date_month = int(self.date.split('-')[1])
				self.date_day = int(self.date.split('-')[2])
				self.test_date_text.setDate(QDate(self.date_year, self.date_month, self.date_day))
				self.test_basis_text.setText(self.edit_result[6].split(':')[1][0:-1])
				self.test_basis_text.setAlignment(QtCore.Qt.AlignCenter)
				self.test_worker_text.setText(self.edit_result[7].split(':')[1][0:-1])
				self.test_worker_text.setAlignment(QtCore.Qt.AlignCenter)
				self.supervise_worker_text.setText(self.edit_result[8].split(':')[1][0:-1])
				self.supervise_worker_text.setAlignment(QtCore.Qt.AlignCenter)

		except IOError:
			print('读取任务信息文件失败!')
		else:
			file.close()
		event.accept()

	def echo_sample_name(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入样品名称：', QLineEdit.Normal)
		self.sample_name_text.setText(value)
		self.sample_name_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_sample_type(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入型号规格：', QLineEdit.Normal)
		self.sample_type_text.setText(value)
		self.sample_type_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_sample_number(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入样品编号：', QLineEdit.Normal)
		self.sample_number_text.setText(value)
		self.sample_number_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_report_number(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入报告编号：', QLineEdit.Normal)
		self.report_number_text.setText(value)
		self.report_number_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_request_company(self):
		value, ok = QInputDialog.getText(self, '新建任务信息', '请输入委托单位：', QLineEdit.Normal)
		self.request_company_text.setText(value)
		self.request_company_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_test_basis(self):
		items = ['GB∕T 36654-2018 76GHz车辆无线电设备射频指标技术要求及测试方法',
		         '毫米波雷达上海市地方标准',
		         '毫米波雷达国家标准',
		         '毫米波雷达企业标准']
		value, ok = QInputDialog.getItem(self, '新建任务信息', '请选择试验依据：', items, 1, True)
		self.test_basis_text.setText(value)
		self.test_basis_text.setAlignment(QtCore.Qt.AlignHCenter)

	def echo_test_worker(self):
		items = ['薛岩', '裴毓', '张晓蕾', '刘力']
		value, ok = QInputDialog.getItem(self, '新建任务信息', '请输入测试人员：', items, 1, True)
		self.test_worker_text.setText(value)
		self.test_worker_text.setAlignment(QtCore.Qt.AlignCenter)

	def echo_supervise_worker(self):
		items = ['薛岩', '裴毓', '张晓蕾', '刘力']
		value, ok = QInputDialog.getItem(self, '新建任务信息', '请输入监督人员：', items, 1, True)
		self.supervise_worker_text.setText(value)
		self.supervise_worker_text.setAlignment(QtCore.Qt.AlignCenter)

	def confirm_information(self):
		file = open('./config/MissionInformation.txt', 'w+')
		file.write(
			'样品名称:{0}\n'
			'型号规格:{1}\n'
			'样品编号:{2}\n'
			'报告编号:{3}\n'
			'委托单位:{4}\n'
			'试验日期:{5}\n'
			'试验依据:{6}\n'
			'测试人员:{7}\n'
			'监督人员:{8}\n'.format(
				self.sample_name_text.toPlainText(),
				self.sample_type_text.toPlainText(),
				self.sample_number_text.toPlainText(),
				self.report_number_text.toPlainText(),
				self.request_company_text.toPlainText(),
				self.test_date_text.date().toString(Qt.ISODate),
				self.test_basis_text.toPlainText(),
				self.test_worker_text.toPlainText(),
				self.supervise_worker_text.toPlainText()))
	# time.sleep(1)
	# self.close()


# 目标模拟器配置菜单
class TargetSimulateMenu(QWidget):
	def __init__(self):
		super(TargetSimulateMenu, self).__init__()

		self.setWindowTitle('目标模拟器设置')
		self.ip_config_label = QLabel('IP地址:')
		self.ip_config_edit = QTextEdit()
		self.ip_config_edit.setMaximumSize(130, 25)
		self.ip_config_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.ip_config_confirm_button = QPushButton('连接')
		self.ip_config_confirm_button.clicked.connect(self.power_supply_connect)
		self.volt_config_label = QLabel('工作电压:')
		self.volt_config_edit = QTextEdit()
		self.volt_config_edit.setMaximumSize(50, 25)
		self.volt_config_edit.setAlignment(QtCore.Qt.AlignCenter)
		self.volt_config_unit_label = QLabel('V')
		self.curr_config_label = QLabel('工作电流:')
		self.curr_config_edit = QTextEdit()
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

	def showEvent(self, event):
		try:
			file = open('./config/TargetSimulate.txt')
			self.config_result = file.readlines()
			self.ip_config_edit.setText(self.config_result[0].split(':')[1][0:-1])
			self.volt_config_edit.setText(self.config_result[2].split(':')[1][0:-2])
			self.curr_config_edit.setText(self.config_result[3].split(':')[1][0:-2])
		except IOError:
			print('读取目标模拟器信息文件失败!')
		else:
			file.close()
		event.accept()

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
		self.result_edit.append('电源连接成功' + time.strftime('%H:%M:%S') + '\n')
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
		self.result_edit.append('完成设置通道：' +
		                        self.power_supply.return_status_chan() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')
		self.result_edit.append('完成设置电压：' +
		                        self.power_supply.return_status_volt() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')
		self.result_edit.append('完成设置电流：' +
		                        self.power_supply.return_status_curr() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')

	def query_result(self):
		self.result_edit.append('当前设置通道：' +
		                        self.power_supply.return_status_chan() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')
		self.result_edit.append('当前设置电压：' +
		                        self.power_supply.return_status_volt() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')
		self.result_edit.append('当前设置电流：' +
		                        self.power_supply.return_status_curr() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')

	def power_on(self):
		self.power_supply.set_output_on()

	def power_off(self):
		self.power_supply.set_output_off()


# 电源模块配置菜单
class PowerSupplyConfig(QWidget):
	def __init__(self):
		super(PowerSupplyConfig, self).__init__()
		self.file = open('./config/PowerSupply.txt', encoding='unicode_escape')
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
		self.result_edit.append('电源连接成功' + time.strftime('%H:%M:%S') + '\n')
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
		self.result_edit.append('完成设置通道：' +
		                        self.power_supply.return_status_chan() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')
		self.result_edit.append('完成设置电压：' +
		                        self.power_supply.return_status_volt() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')
		self.result_edit.append('完成设置电流：' +
		                        self.power_supply.return_status_curr() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')

	def query_result(self):
		self.result_edit.append('当前设置通道：' +
		                        self.power_supply.return_status_chan() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')
		self.result_edit.append('当前设置电压：' +
		                        self.power_supply.return_status_volt() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')
		self.result_edit.append('当前设置电流：' +
		                        self.power_supply.return_status_curr() + 'V ' +
		                        time.strftime('%H:%M:%S') + '\n')

	def power_on(self):
		self.power_supply.set_output_on()

	def power_off(self):
		self.power_supply.set_output_off()


# 转台模块配置菜单
class TurnTableConfig(QWidget):
	def __init__(self):
		super(TurnTableConfig, self).__init__()
		self.file = open('./config/TurnTable.txt', encoding='unicode_escape')
		self.config_result = self.file.readlines()
		# self.turn_table = TurnTable()
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
		self.azimuth_current_angle_text = QTextBrowser()
		self.azimuth_current_angle_text.setMaximumSize(70, 25)
		self.azimuth_current_angle_text.setAlignment(QtCore.Qt.AlignCenter)
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
		self.pitching_current_angle_text = QTextBrowser()
		self.pitching_current_angle_text.setMaximumSize(70, 25)
		self.pitching_current_angle_text.setAlignment(QtCore.Qt.AlignCenter)
		self.pitching_current_unit_label = QLabel('°')
		self.azimuth_relative_edit.setEnabled(True)
		self.pitching_relative_edit.setEnabled(True)
		self.azimuth_absolute_edit.setEnabled(False)
		self.pitching_absolute_edit.setEnabled(False)
		self.connect_button = QPushButton('连接')
		self.connect_button.clicked.connect(self.turn_table_status)
		self.find_home_combo = QComboBox()
		self.find_home_combo.addItems(('水平寻零', '俯仰寻零', '全向寻零'))
		self.find_home_button = QPushButton('开始寻零')
		self.find_home_button.setEnabled(False)
		self.find_home_button.clicked.connect(self.find_home)
		self.confirm_button = QPushButton('开始旋转')
		self.confirm_button.setEnabled(False)
		self.confirm_button.clicked.connect(self.confirm_config)
		self.result_label = QLabel('系统状态')
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
		self.down_grid_layout.addWidget(self.azimuth_current_angle_text, 1, 5, 1, 1)
		self.down_grid_layout.addWidget(self.azimuth_current_unit_label, 1, 6, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_motion_label, 2, 0, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_relative_edit, 2, 1, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_relative_unit_label, 2, 2, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_absolute_edit, 2, 3, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_absolute_unit_label, 2, 4, 1, 1)
		self.down_grid_layout.addWidget(self.pitching_current_angle_text, 2, 5, 1, 1)
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
			self.result_edit.append('转台连接成功')
			self.turn_table.connect()
			self.azimuth_current_angle = CurrentAngleAzimuth()
			self.pitching_current_angle = CurrentAnglePitching()
			self.azimuth_current_angle.start()
			self.pitching_current_angle.start()
			self.azimuth_current_angle.my_signal.connect(self.azimuth_current_angle_display)
			self.pitching_current_angle.my_signal.connect(self.pitching_current_angle_display)
			self.connect_button.setText('断开')
			if self.manual_config_button.isChecked():
				self.find_home_button.setEnabled(True)
				self.confirm_button.setEnabled(True)
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
				self.find_home_button.setEnabled(False)
				self.confirm_button.setEnabled(False)
				self.azimuth_relative_edit.setEnabled(False)
				self.pitching_relative_edit.setEnabled(False)
				self.azimuth_absolute_edit.setEnabled(False)
				self.pitching_absolute_edit.setEnabled(False)
		else:
			self.result_edit.append('转台断开连接')
			self.azimuth_current_angle.quit()
			self.pitching_current_angle.quit()
			self.turn_table.disconnect()
			self.find_home_button.setEnabled(False)
			self.confirm_button.setEnabled(False)
			self.azimuth_current_angle_text.setText('')
			self.pitching_current_angle_text.setText('')
			self.connect_button.setText('连接')

	def find_home(self):
		if self.find_home_combo.currentText() == '水平寻零':
			self.turn_table.s_home(2)
			self.azimuth_find_home = FindHome(2)
			self.azimuth_find_home.start()
			self.azimuth_find_home.my_signal.connect(self.find_home_result_display)
		elif self.find_home_combo.currentText() == '俯仰寻零':
			self.turn_table.s_home(1)
			self.pitching_find_home = FindHome(1)
			self.pitching_find_home.start()
			self.pitching_find_home.my_signal.connect(self.find_home_result_display)
		else:
			self.turn_table.s_home(2)
			self.azimuth_find_home = FindHome(2)
			self.azimuth_find_home.start()
			self.azimuth_find_home.my_signal.connect(self.find_home_result_display)
			self.turn_table.s_home(1)
			self.pitching_find_home = FindHome(1)
			self.pitching_find_home.start()
			self.pitching_find_home.my_signal.connect(self.find_home_result_display)

	def mode_select(self):
		if self.connect_button.text() == '断开':
			if self.manual_config_button.isChecked():
				self.find_home_button.setEnabled(True)
				self.confirm_button.setEnabled(True)
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
				self.find_home_button.setEnabled(False)
				self.confirm_button.setEnabled(False)

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

	def manual_motion(self):
		if self.relative_motion_button.isChecked():
			self.turn_table.move_to_position(2, float(self.azimuth_relative_edit.toPlainText()), 1, False)
			self.turn_table.move_to_position(1, float(self.pitching_relative_edit.toPlainText()), 1, False)
		else:
			self.turn_table.move_to_position(2, float(self.azimuth_absolute_edit.toPlainText()), 1, True)
			self.turn_table.move_to_position(1, float(self.pitching_absolute_edit.toPlainText()), 1, True)

	def find_home_result_display(self, message):
		self.result_edit.append(message)

	def azimuth_current_angle_display(self, message):
		self.azimuth_current_angle_text.setText(message)

	def pitching_current_angle_display(self, message):
		self.pitching_current_angle_text.setText(message)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	radar_test = RadarTestMain()
	radar_test.show()
	sys.exit(app.exec())
