import sys
import MainWindow as u1
import MessageWindow as u2
from PyQt5.QtWidgets import *


class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.ui = u2.Ui_Form()
        self.ui.setupUi(self)

    def slot1(self):
        win2.close()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = u1.Ui_MainWindow()
        self.ui.setupUi(self)

    def slot1(self):
        win2.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win2 = SecondWindow()
    sys.exit(app.exec_())