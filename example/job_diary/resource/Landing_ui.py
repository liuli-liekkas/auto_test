# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Landing.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 200)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(50, 30, 50, 30)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.lable = QtWidgets.QLabel(Form)
        self.lable.setObjectName("lable")
        self.gridLayout.addWidget(self.lable, 0, 0, 1, 1)
        self.name_le = QtWidgets.QLineEdit(Form)
        self.name_le.setText("")
        self.name_le.setObjectName("name_le")
        self.gridLayout.addWidget(self.name_le, 0, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)
        self.password_le = QtWidgets.QLineEdit(Form)
        self.password_le.setText("")
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setObjectName("password_le")
        self.gridLayout.addWidget(self.password_le, 1, 1, 1, 1)
        self.landing_btn = QtWidgets.QPushButton(Form)
        self.landing_btn.setEnabled(False)
        self.landing_btn.setMinimumSize(QtCore.QSize(100, 35))
        self.landing_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius:5px;\n"
"    color:white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(72,203,250);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85,85,255);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(167,167,167);\n"
"}")
        self.landing_btn.setFlat(False)
        self.landing_btn.setObjectName("landing_btn")
        self.gridLayout.addWidget(self.landing_btn, 2, 0, 1, 2)

        self.retranslateUi(Form)
        self.name_le.textChanged['QString'].connect(Form.btn_sate_le)
        self.password_le.textChanged['QString'].connect(Form.btn_sate_le)
        self.landing_btn.clicked.connect(Form.land_btn)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.name_le, self.password_le)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lable.setText(_translate("Form", "用户名"))
        self.name_le.setPlaceholderText(_translate("Form", "请输入用户名！"))
        self.label_1.setText(_translate("Form", "密 码"))
        self.password_le.setPlaceholderText(_translate("Form", "请输入密码！"))
        self.landing_btn.setText(_translate("Form", "登陆"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

