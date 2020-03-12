from PyQt5.QtWidgets import QMainWindow, QComboBox, QPushButton,QHBoxLayout
import radar_test

class SelectWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.okButton.clicked.connect(self.slot_btn_function)

    def slot_btn_function(self):
        select_value = self.combo.currentText()
        self.radar_test = radar_test.RadarTest()
        if select_value == "毫米波雷达测试系统":
            self.close()
            self.radar_test.show()

    def init_ui(self):
        self.h_select = QHBoxLayout()
        self.combo = QComboBox(self)
        self.combo.addItem("毫米波雷达测试系统")
        self.combo.addItem("导航模块测试系统")
        self.combo.addItem("通信模块测试系统")
        self.combo.addItem("保险杠测试系统")
        self.combo.addItem("摄像头测试系统")
        self.okButton = QPushButton("确定", self)
        self.h_select.addWidget(self.combo)
        self.h_select.addWidget(self.okButton)
        self.resize(400, 200)
        self.setWindowTitle("选择测试分系统")
