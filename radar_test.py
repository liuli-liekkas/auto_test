from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QFileDialog, qApp, QMenu, QWidget, QLineEdit, QRadioButton, QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, QCheckBox, QTabWidget, QApplication, QPushButton, QDateEdit, QComboBox, QTextEdit, QTableWidget, QGridLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
import sys
import datetime


class RadarTest(QMainWindow):
    def __init__(self):
        super(RadarTest, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(1200, 800)
        self.center()
        self.statusBar().showMessage("测试人：刘力")
        self.setWindowTitle("毫米波雷达测试系统")
        self.setFont(QFont('Menlo', 12))
        self.menu_init()
        # self.tool_menu_init()
        self.tab_menu()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def menu_init(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("文件")
        edit_menu = menubar.addMenu("编辑")
        view_menu = menubar.addMenu("视图")
        config_menu = menubar.addMenu("配置")
        analysis_menu = menubar.addMenu("分析")
        self_test_menu = menubar.addMenu("自检")
        tool_menu = menubar.addMenu("工具")
        help_menu = menubar.addMenu("帮助")

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

    def tab_menu(self):
        self.central_widget = QWidget(self)
        self.tabWidget = QTabWidget(self.central_widget)
        self.tabWidget.setGeometry(0, 0, self.width()-100, self.height()-100)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabWidget.addTab(self.tab1, "射频性能测试")
        self.tabWidget.addTab(self.tab2, "探测性能测试")
        self.tabWidget.addTab(self.tab3, "天线性能测试")
        self.setCentralWidget(self.central_widget)
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()

    def tab1_ui(self):
        self.off_button = QRadioButton('off', self)
        self.on_button = QRadioButton('on', self)
        self.pic_label = QLabel(self)

        self.name_label = QLabel('姓名')
        self.department_label = QLabel('部门')
        self.post_label = QLabel('岗位')
        self.name_edit = QLineEdit()
        self.department_edit = QLineEdit()
        self.post_edit = QLineEdit()

        self.time_label = QLabel('时间')
        self.job_classify_label = QLabel('工作分类')
        self.man_hour_label = QLabel('工时')
        self.nature_label = QLabel('性质')
        self.important_urgency_label = QLabel('重要/紧急')
        self.status_label = QLabel('状态')
        self.work_cop_label = QLabel('工作配合')
        self.time_data_edit = QDateEdit()
        self.time_data_edit.setCalendarPopup(True)
        self.time_data_edit.setDate(QtCore.QDate(2020, 1, 1))
        self.job_classify_combo = QComboBox()
        self.man_hour_combo = QComboBox()
        self.nature_combo = QComboBox()
        self.important_urgency_combo = QComboBox()
        self.status_combo = QComboBox()
        self.work_cop_combo = QComboBox()

        self.content_label = QLabel()
        self.question_label = QLabel()
        self.content_edit = QTextEdit()
        self.question_edit = QTextEdit()

        self.save_button = QPushButton('保存', self)
        self.change_button = QPushButton('修改', self)
        self.delete_button = QPushButton('删除', self)
        self.submit_button = QPushButton('提交', self)
        self.query_button = QPushButton('查询', self)
        self.config_button = QPushButton('配置', self)

        self.message_table = QTableWidget()
        self.message_table.setHorizontalHeaderLabels(['时间', '工作分类', '事项内容', '工时', '性质', '重要/紧急', '状态', '工作配合', '问题和困难', 'ID'])

        self.tab1_layout_init()
        self.radiobutton_init()
        self.label_init()

    def tab1_layout_init(self):
        self.up_h_layout = QHBoxLayout()
        self.up_h_layout.addWidget(self.name_label)
        self.up_h_layout.addWidget(self.name_edit)
        self.up_h_layout.addWidget(self.department_label)
        self.up_h_layout.addWidget(self.department_edit)
        self.up_h_layout.addWidget(self.post_label)
        self.up_h_layout.addWidget(self.post_edit)
        self.up_h_layout.addStretch(3)
        self.up_h_layout.setStretch(3, 1)

        self.l_grid_layout = QGridLayout()
        self.l_grid_layout.addWidget(self.time_label, 0, 0, 1, 1)
        self.l_grid_layout.addWidget(self.time_data_edit, 0, 1, 1, 1)
        self.l_grid_layout.addWidget(self.job_classify_label, 1, 0, 1, 1)
        self.l_grid_layout.addWidget(self.job_classify_combo, 1, 1, 1, 1)
        self.l_grid_layout.addWidget(self.man_hour_label, 2, 0, 1, 1)
        self.l_grid_layout.addWidget(self.man_hour_combo, 2, 1, 1, 1)
        self.l_grid_layout.addWidget(self.nature_label, 3, 0, 1, 1)
        self.l_grid_layout.addWidget(self.nature_combo, 3, 1, 1, 1)
        self.l_grid_layout.addWidget(self.important_urgency_label, 4, 0, 1, 1)
        self.l_grid_layout.addWidget(self.important_urgency_combo, 4, 1, 1, 1)
        self.l_grid_layout.addWidget(self.status_label, 5, 0, 1, 1)
        self.l_grid_layout.addWidget(self.status_combo, 5, 1, 1, 1)
        self.l_grid_layout.addWidget(self.work_cop_label, 6, 0, 1, 1)
        self.l_grid_layout.addWidget(self.work_cop_combo, 6, 1, 1, 1)

        self.button_h_layout = QHBoxLayout()
        self.pic_h_layout = QHBoxLayout()
        self.pic_h_layout.addStretch(1)
        self.pic_h_layout.addWidget(self.pic_label)
        self.pic_h_layout.addStretch(1)
        self.button_h_layout.addWidget(self.off_button)
        self.button_h_layout.addWidget(self.on_button)
        # self.all_v_layout.addLayout(self.up_h_layout)
        # self.all_v_layout.addLayout(self.pic_h_layout)
        # self.all_v_layout.addLayout(self.button_h_layout)
        # self.tab1.setLayout(self.all_v_layout)

        self.all_v_layout = QVBoxLayout()
        self.all_v_layout.addLayout(self.up_h_layout)
        self.all_v_layout.addLayout(self.l_grid_layout)
        self.all_v_layout.addLayout(self.pic_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)
        self.all_v_layout.addWidget(self.message_table)
        self.tab1.setLayout(self.all_v_layout)

    def radiobutton_init(self):
        self.off_button.setChecked(True)
        self.off_button.toggled.connect(self.on_off_bulb_func)

    def label_init(self):
        self.pic_label.setPixmap((QPixmap('./image/light_off.png')))

    def on_off_bulb_func(self):
        if self.off_button.isChecked():
            self.pic_label.setPixmap(QPixmap('./image/light_off.png'))
        else:
            self.pic_label.setPixmap(QPixmap('./image/light_on.png'))

    def tab2_ui(self):
        pass

    def tab3_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    radar_test = RadarTest()
    radar_test.show()
    sys.exit(app.exec())
