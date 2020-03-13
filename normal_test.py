import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class CheckBoxDemo(QWidget):

    def __init__(self, parent=None):
        super(CheckBoxDemo, self).__init__(parent)

        #创建一个GroupBox组
        groupBox = QGroupBox("Checkboxes")
        groupBox.setFlat(False)

        #创建复选框1，并默认选中，当状态改变时信号触发事件
        self.checkBox1 = QCheckBox("&Checkbox1")
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda: self.btnstate(self.checkBox1))

        #创建复选框，标记状态改变时信号触发事件
        self.checkBox2 = QCheckBox("Checkbox2")
        self.checkBox2.toggled.connect(lambda: self.btnstate(self.checkBox2))

        #创建复选框3，设置为3状态，设置默认选中状态为半选状态，当状态改变时信号触发事件
        self.checkBox3 = QCheckBox("tristateBox")
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(lambda: self.btnstate(self.checkBox3))

        #水平布局
        layout = QHBoxLayout()
        #控件添加到水平布局中
        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.checkBox3)

        #设置QGroupBox组的布局方式
        groupBox.setLayout(layout)

        #设置主界面布局垂直布局
        mainLayout = QVBoxLayout()
        #QgroupBox的控件添加到主界面布局中
        mainLayout.addWidget(groupBox)

        #设置主界面布局
        self.setLayout(mainLayout)
        #设置主界面标题
        self.setWindowTitle("checkbox demo")

    #输出三个复选框当前的状态，0选中，1半选，2没选中
    def btnstate(self, btn):
        chk1Status = self.checkBox1.text() + ", isChecked=" + str(self.checkBox1.isChecked()) + ', chekState=' + str(
            self.checkBox1.checkState()) + "\n"
        chk2Status = self.checkBox2.text() + ", isChecked=" + str(self.checkBox2.isChecked()) + ', checkState=' + str(
            self.checkBox2.checkState()) + "\n"
        chk3Status = self.checkBox3.text() + ", isChecked=" + str(self.checkBox3.isChecked()) + ', checkState=' + str(
            self.checkBox3.checkState()) + "\n"
        print(chk1Status + chk2Status + chk3Status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkboxDemo = CheckBoxDemo()
    checkboxDemo.show()
    sys.exit(app.exec_())
