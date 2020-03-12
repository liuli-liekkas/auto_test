from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QFileDialog, qApp, QMenu, QWidget, QLineEdit, QRadioButton, QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, QCheckBox, QTabWidget, QApplication, QPushButton
from PyQt5.QtGui import QFont, QPixmap
import sys


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
        selftest_menu = menubar.addMenu("自检")
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

        self.save_button = QPushButton('保存', self)
        self.change_button = QPushButton('修改', self)
        self.delete_button = QPushButton('删除', self)
        self.submit_button = QPushButton('提交', self)
        self.query_button = QPushButton('查询', self)
        self.config_button = QPushButton('配置', self)

        self.name_label = QLabel('姓名')

        self.button_h_layout = QHBoxLayout()
        self.pic_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()
        self.tab1_layout_init()
        self.radiobutton_init()
        self.label_init()

    def tab1_layout_init(self):
        self.pic_h_layout.addStretch(1)
        self.pic_h_layout.addWidget(self.pic_label)
        self.pic_h_layout.addStretch(1)
        self.button_h_layout.addWidget(self.off_button)
        self.button_h_layout.addWidget(self.on_button)
        self.all_v_layout.addLayout(self.pic_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)
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