from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
import sys
import pyqtgraph as pg


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
        open_act.triggered.connect(self.open_file)
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
        self.central_widget = QWidget(self)
        self.tabWidget = QTabWidget(self.central_widget)
        # self.tabWidget.setGeometry(0, 0, self.width(), self.height()-50)
        self.tabWidget.setStyleSheet("QTabBar::tab:selected{color:red;background-color:rbg(200,200,255);} ")
        self.tabWidget.setFont(QFont('KaiTi', 16))
        # self.tabWidget.set
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
        self.tab2_horizontal_power_config_button.clicked.connect(self.horizontal_power_config_menu_window_display)
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

    def horizontal_power_config_menu_window_display(self):
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
        self.file = open('./config/HorizontalPowerTest.txt', 'r')
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
        self.min_angle_edit.setText(self.edit_result[3].split(':')[1][0:-2])
        self.min_angle_edit.setMaximumSize(50, 25)
        self.min_angle_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.min_angle_unit_label = QLabel('°')
        self.max_angle_label = QLabel('最大测试角度')
        self.max_angle_edit = QTextEdit()
        self.max_angle_edit.setText(self.edit_result[4].split(':')[1][0:-2])
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
        self.confirm_button.clicked.connect(self.set_result__confirm)
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

    def set_result__confirm(self):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    radar_test = RadarTestMain()
    radar_test.show()
    sys.exit(app.exec())
