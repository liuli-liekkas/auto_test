import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QTextEdit, \
                            QApplication, QFrame, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QVBoxLayout(self)
        self.setWindowTitle('QSplitter')
        self.setGeometry(300, 300, 300, 200)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bt1 = QPushButton(topleft)
        bt1.setText('hello')
        tx1 = QTextEdit(topleft)
        tx1.setText('test')
        hlayout = QHBoxLayout()
        hlayout.addWidget(bt1)
        hlayout.addWidget(tx1)
        topleft.setLayout(hlayout)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        sp1 = QSplitter(Qt.Horizontal)
        te = QTextEdit()
        sp1.addWidget(topleft)
        sp1.addWidget(te)
        sp1.setSizes([100, 200])

        sp2 = QSplitter(Qt.Vertical)
        sp2.addWidget(sp1)
        sp2.addWidget(bottom)

        hbox.addWidget(sp2)
        self.setLayout(hbox)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())