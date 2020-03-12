import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.off_button = QRadioButton('off', self)                 # 1
        self.on_button = QRadioButton('on', self)                   # 2

        self.pic_label = QLabel(self)                               # 3

        self.button_h_layout = QHBoxLayout()
        self.pic_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.pic_h_layout.addStretch(1)                             # 4
        self.pic_h_layout.addWidget(self.pic_label)
        self.pic_h_layout.addStretch(1)
        self.button_h_layout.addWidget(self.off_button)
        self.button_h_layout.addWidget(self.on_button)
        self.all_v_layout.addLayout(self.pic_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)

    def radiobutton_init(self):
        self.off_button.setChecked(True)                            # 5
        self.off_button.toggled.connect(self.on_off_bulb_func)      # 6
        # self.on_button.toggled.connect(self.on_off_bulb_func)

    def label_init(self):
        self.pic_label.setPixmap(QPixmap('./image/light_off.png'))                # 7

    def on_off_bulb_func(self):                                     # 8
        if self.off_button.isChecked():
            self.pic_label.setPixmap(QPixmap('./image/light_off.png'))
        else:
            self.pic_label.setPixmap(QPixmap('./image/light_on.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())