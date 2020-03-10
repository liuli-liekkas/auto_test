import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 130)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(80, 50, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(190, 50, 75, 23))
        self.okButton.setObjectName("okButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ComboBox下拉框例子"))
        self.comboBox.setItemText(0, _translate("Form", "Python"))
        self.comboBox.setItemText(1, _translate("Form", "C++"))
        self.comboBox.setItemText(2, _translate("Form", "Go"))
        self.comboBox.setItemText(3, _translate("Form", "Java"))
        self.okButton.setText(_translate("Form", "确定"))


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.getComboxBoxValue)

    def getComboxBoxValue(self):
        select_value = self.comboBox.currentText()
        QMessageBox.information(self, "消息框标题", "你要学%s,为师给你说道说道！" % (select_value,), QMessageBox.Yes | QMessageBox.No)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
