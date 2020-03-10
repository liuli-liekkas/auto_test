import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("智能传感器室自动化测试系统")
        self.resize(500, 200)
        self.Password = "1"
        self.UserName = "ll"
        self.Co_Width = 40
        self.Co_Height = 20
        self.init_ui()

    def init_ui(self):
        self.lab_l = QLabel("帐户:", self)
        self.Lin_l = QLineEdit(self)
        self.lab_p = QLabel("密码:", self)
        self.Lin_p = QLineEdit(self)
        self.Lin_p.setEchoMode(QLineEdit.Password)
        self.Pu_l = QPushButton("登陆", self)
        self.Pu_l.clicked.connect(self.login)

    def resizeEvent(self, evt):
        self.lab_l.resize(self.Co_Width, self.Co_Height)
        self.lab_l.move(self.width()/3, self.height()/5)
        self.Lin_l.move(self.lab_l.x()+self.lab_l.width(), self.lab_l.y())
        self.lab_p.resize(self.Co_Width, self.Co_Height)
        self.lab_p.move(self.lab_l.x(), self.lab_l.y()+self.lab_l.height()*2)
        self.Lin_p.move(self.lab_p.x()+self.lab_p.width(), self.lab_p.y())
        self.Pu_l.move(self.Lin_p.x()+self.Lin_p.width()/4, self.lab_p.y()+self.lab_p.height()*2)

    def login(self):
        if self.Lin_l.text() == self.UserName and self.Lin_p.text() == self.Password:
            print("登陆成功!!")
            self.slot_btn_function()
        elif self.Lin_l.text() != self.UserName:
            self.Lin_l.setText("")
            self.Lin_p.setText("")
            print("帐户录入错误!!")
        elif self.Lin_p.text() != self.Password:
            self.Lin_p.setText("")
            print("密码录入错误!!")

    def slot_btn_function(self):
        self.hide()
        self.s = SelectWindow()
        self.s.show()


class UiForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 130)
        self.comboBox = QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 50, 170, 40))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.okButton = QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(250, 50, 75, 40))
        self.okButton.setObjectName("okButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "选择测试分系统"))
        self.comboBox.setItemText(0, _translate("Form", "毫米波雷达测试系统"))
        self.comboBox.setItemText(1, _translate("Form", "导航模块测试系统"))
        self.comboBox.setItemText(2, _translate("Form", "通信模块测试系统"))
        self.comboBox.setItemText(3, _translate("Form", "保险杠测试系统"))
        self.comboBox.setItemText(4, _translate("Form", "摄像头测试系统"))
        self.okButton.setText(_translate("Form", "确定"))


class SelectWindow(QMainWindow, UiForm):
    def __init__(self, parent=None):
        super(SelectWindow, self).__init__(parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.slot_btn_function)

    def slot_btn_function(self):
        select_value = self.comboBox.currentText()
        if select_value == "毫米波雷达测试系统":
            self.hide()
            self.r = RadarTest()
            self.r.show()


class RadarTest(QMainWindow):
    def __init__(self, parent=None):
        super(RadarTest, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 1200, 800)
        self.statusBar().showMessage("测试人：刘力")
        self.setWindowTitle("毫米波雷达测试系统")
        self.menu_init()
        # self.tool_menu_init()
        self.tab_menu()
        self.show()

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

        open_menu = QMenu("打开", self)
        new_act = QAction("New", self, checkable=True)
        open_menu.addAction(new_act)
        file_menu.addMenu(open_menu)

        com_act = QAction("串口调试", self)
        com_act.setStatusTip("打开串口调试工具")
        # com_act.triggered.connect()
        tool_menu.addAction(com_act)

        net_act = QAction("网口调试", self)
        net_act.setStatusTip("打开网口调试工具")
        # net_act.triggered.connect()
        tool_menu.addAction(net_act)

    def contextMenuEvent(self, e):
        cmenu = QMenu(self)
        new_act = cmenu.addAction("new")
        open_act = cmenu.addAction("Open")
        quit_act = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(e.pos()))
        if action == quit_act:
            qApp.quit()

    # def tool_menu_init(self):
    #     exit_act = QAction("退出", self)
    #     exit_act.setShortcut("Ctrl+Q")
    #     exit_act.triggered.connect(qApp.quit)
    #     exit_act.setToolTip("退出应用")
    #
    #     self.toolbar = self.addToolBar("exit")
    #     self.toolbar.addAction(exit_act)

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


if __name__ == '__main__':
    App = QApplication(sys.argv)
    Win = RadarTest()
    Win.show()
    sys.exit(App.exec_())


