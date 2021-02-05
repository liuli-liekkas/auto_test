#coding=utf8
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DateDialog(QDialog):
    # 信号的定义
    Signal_parp = pyqtSignal(str)
    def __init__(self,parent=None):
        super(DateDialog,self).__init__(parent)
        self.setWindowTitle("DataDialog")
        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)

        button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        button.accepted.connect(self.accept)
        button.rejected.connect(self.reject)
        layout.addWidget(button)

        self.button = QPushButton("发送")

        # self.button.clicked.connect(self.onClickButton)
        # 日历控件时间改变的事件和之前的clicked事件是一样的都需要绑定槽函数
        self.datetime.dateTimeChanged.connect(self.onClickButton)

        # 使用按键触发---来导致信号触发
        self.button.clicked.connect(self.buttonClicked)
        layout.addWidget(self.button)
    # 信号的触发可以通过其他控件来触发----控件本身就有触发机制
    def onClickButton(self):
        data_str = self.datetime.dateTime().toString()
        print("触发了")
        print(data_str)
        # 信号的触发
        self.Signal_parp.emit(data_str)
    # 按键触发---->导致信号触发试试
    def buttonClicked(self):
        data_str = self.datetime.dateTime().toString()
        self.Signal_parp.emit(data_str)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent = None):
        dialog = DateDialog(parent)
        result = dialog.exec()
        date = dialog.dateTime()
        return (date.date(),date.time(),result == QDialog.Accepted)