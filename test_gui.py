import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QAction, qApp
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon


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
        self.hide()
        self.r = RadarTest()
        self.r.show()


class RadarTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    Win = LoginWindow()
    Win.show()
    sys.exit(App.exec_())


