# import sys
# import MainWindow as u1
# import MessageWindow as u2
# from PyQt5.QtWidgets import *
#
#
# class SecondWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(SecondWindow, self).__init__(parent)
#         self.ui = u2.Ui_Form()
#         self.ui.setupUi(self)
#
#     def slot1(self):
#         win2.close()
#
#
# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.ui = u1.Ui_MainWindow()
#         self.ui.setupUi(self)
#
#     def slot1(self):
#         win2.show()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     win2 = SecondWindow()
#     sys.exit(app.exec_())


#coding=utf8
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
"""
多窗口交互---直接访问对应的控件，代码的耦合度高
方式1 直接访问控件
"""

# from DataDialog import DateDialog
#
# class MultiWindow1(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle(" 多窗口交互")
#
#         self.lineEdit = QLineEdit(self)
#         self.button1 = QPushButton('弹出对话框1')
#         self.button1.clicked.connect(self.onButton1Click)
#
#         self.button2 = QPushButton('弹出对话框2')
#         self.button2.clicked.connect(self.onButton2Click)
#
#         gridLayout = QGridLayout()
#         gridLayout.addWidget(self.button1)
#         gridLayout.addWidget(self.button2)
#         gridLayout.addWidget(self.lineEdit)
#
#         self.setLayout(gridLayout)
#
#     def onButton1Click(self):
#         dialog = DateDialog(self)
#         # 对话框保持悬浮
#         result = dialog.exec()
#         date = dialog.dateTime()
#         self.lineEdit.setText(date.date().toString())
#         dialog.destroy()
#
#     def onButton2Click(self):
#         date,time,result = DateDialog.getDateTime()
#         self.lineEdit.setText(date.toString())
#         if result == QDialog.Accepted:
#             print("点击确定按钮")
#         else:
#             print('单击取消按钮')
"""
多窗口交互，使用信号与槽函数
这样就可以降低代码的耦合度： 信号：创建、触发、连接
"""
from DataDialog import DateDialog

class MultiWindow1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" 多窗口交互")

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Click)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)
        gridLayout.addWidget(self.lineEdit)

        self.setLayout(gridLayout)

    def onButton1Click(self):
        dialog = DateDialog(self)
        """
        这是直接访问
        """
        # date = dialog.dateTime()
        # self.lineEdit.setText(date.date().toString())
        """
        使用信号访问,信号连接槽,,多窗口交互的时候尽量使用信号来传数据--尽量避免直接访问控件
        创建---在子窗口
        触发---在子窗口
        信号一旦触发就会执行绑定的槽函数------所以说用信号来传输数据是最佳的载体
        绑定---在主窗口
        """
        # 绑定
        dialog.Signal_parp.connect(self.deal_emit_slot)
        dialog.show()
        # dialog.destroy()

    def deal_emit_slot(self,datestr):
        # self.lineEdit.setText("1234")
        self.lineEdit.setText(datestr)

    def onButton2Click(self):
        date,time,result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result == QDialog.Accepted:
            print("点击确定按钮")
        else:
            print('单击取消按钮')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MultiWindow1()
    window.show()
    app.exec_()