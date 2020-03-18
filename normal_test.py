import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(-99, 99)                                                      # 1
        self.spinbox.setSingleStep(1)                                                       # 2
        self.spinbox.setValue(66)                                                           # 3
        self.spinbox.valueChanged.connect(self.value_change_func)                           # 4

        self.double_spinbox = QDoubleSpinBox(self)                                          # 5
        self.double_spinbox.setRange(-99.99, 99.99)
        self.double_spinbox.setSingleStep(0.01)
        self.double_spinbox.setValue(66.66)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.spinbox)
        self.h_layout.addWidget(self.double_spinbox)
        self.setLayout(self.h_layout)

    def value_change_func(self):
        decimal_part = self.double_spinbox.value() - int(self.double_spinbox.value())       # 6
        self.double_spinbox.setValue(self.spinbox.value() + decimal_part)                   # 7


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())