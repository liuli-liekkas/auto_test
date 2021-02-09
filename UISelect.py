from PyQt5.QtWidgets import *
import UIRadarTest
import sys


class SelectWindow(QWidget):
    def __init__(self):
        super(SelectWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("选择测试分系统")
        self.resize(400, 120)
        self.combo = QComboBox(self)
        self.combo.setMinimumSize(200, 30)
        self.combo.addItem("--请选择--")
        self.combo.addItem("毫米波雷达测试系统")
        self.combo.addItem("导航模块测试系统")
        self.combo.addItem("通信模块测试系统")
        self.combo.addItem("保险杠测试系统")
        self.combo.addItem("摄像头测试系统")
        self.combo.setView(QListView())
        self.okButton = QPushButton("确定", self)
        self.okButton.clicked.connect(self.slot_btn_function)
        self.layout_init()

    def layout_init(self):
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.combo)
        self.h_layout.addWidget(self.okButton)
        self.setLayout(self.h_layout)

    def slot_btn_function(self):
        select_value = self.combo.currentText()
        if select_value == "毫米波雷达测试系统":
            self.close()
            self.radar_test = UIRadarTest.RadarTestMain()
            self.radar_test.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    select_window = SelectWindow()
    select_window.show()
    sys.exit(app.exec())
