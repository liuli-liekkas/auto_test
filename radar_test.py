from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QFileDialog, qApp, QMenu, QWidget, QLineEdit, QRadioButton, QHBoxLayout, QFormLayout, QLabel, QCheckBox, QTabWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QFont


class RadarTest(QMainWindow):
    def __init__(self, parent=None):
        super(RadarTest, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.resize(1200, 800)
        self.center()
        self.statusBar().showMessage("测试人：刘力")
        self.setWindowTitle("毫米波雷达测试系统")
        self.setFont(QFont('Menlo', 16))
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

        exit_act = QAction("退出", self)
        exit_act.setShortcut("Ctrl+Q")
        exit_act.setStatusTip("退出应用程序")
        exit_act.triggered.connect(qApp.quit)
        file_menu.addAction(exit_act)

        open_menu = QAction("打开", self)
        open_menu.setShortcut('Ctrl+O')
        exit_act.setStatusTip("打开文件")
        open_menu.triggered.connect(self.show_dialog)
        file_menu.addAction(open_menu)

        com_act = QAction("串口调试", self)
        com_act.setStatusTip("打开串口调试工具")
        # com_act.triggered.connect()
        tool_menu.addAction(com_act)

        net_act = QAction("网口调试", self)
        net_act.setStatusTip("打开网口调试工具")
        # net_act.triggered.connect()
        tool_menu.addAction(net_act)

    def show_dialog(self):
        QFileDialog.getOpenFileName(self, '打开文件', '/home')

    def contextMenuEvent(self, e):
        cmenu = QMenu(self)
        new_act = cmenu.addAction("new")
        open_act = cmenu.addAction("Open")
        quit_act = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(e.pos()))
        if action == quit_act:
            qApp.quit()

    def tool_menu_init(self):
        exit_act = QAction("退出", self)
        exit_act.setShortcut("Ctrl+Q")
        exit_act.triggered.connect(qApp.quit)
        exit_act.setToolTip("退出应用")

        self.toolbar = self.addToolBar("exit")
        self.toolbar.addAction(exit_act)

    def tab_menu(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QWidget()
        self.tab1.setObjectName("tab1")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName("tab2")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName("tab3")
        self.tabWidget.addTab(self.tab3, "")
        self.setCentralWidget(self.centralwidget)
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()

    def tab1_ui(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.tabWidget.setTabText(0, "射频性能测试")
        self.tab1.setLayout(layout)

    def tab2_ui(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.tabWidget.setTabText(1, "探测性能测试")
        self.tab2.setLayout(layout)

    def tab3_ui(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.tabWidget.setTabText(2, "天线性能测试")
        self.tab3.setLayout(layout)