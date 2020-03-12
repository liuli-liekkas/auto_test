from PyQt5.QtWidgets import QMainWindow, QComboBox, QPushButton, QApplication, QListView
import radar_test
import sys


class SelectWindow(QMainWindow):
    def __init__(self):
        super(SelectWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("选择测试分系统")
        self.resize(400, 120)
        self.combo = QComboBox(self)
        self.combo.move(30, 40)
        self.combo.setMinimumSize(200, 20)
        self.combo.addItem("--请选择--")
        self.combo.addItem("毫米波雷达测试系统")
        self.combo.addItem("导航模块测试系统")
        self.combo.addItem("通信模块测试系统")
        self.combo.addItem("保险杠测试系统")
        self.combo.addItem("摄像头测试系统")
        self.combo.setView(QListView())
        self.okButton = QPushButton("确定", self)
        self.okButton.move(260, 40)
        self.okButton.clicked.connect(self.slot_btn_function)

    def slot_btn_function(self):
        select_value = self.combo.currentText()
        if select_value == "毫米波雷达测试系统":
            self.close()
            self.radar_test = radar_test.RadarTest()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    select_window = SelectWindow()
    select_window.show()
    sys.exit(app.exec())
