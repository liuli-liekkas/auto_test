from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal,Qt
import sys
import pyqtgraph as pg
from MachineClass import *

class Ui_MainWindow(QMainWindow):
	def __init__(self):
		super(Ui_MainWindow, self).__init__()
		self.resize(800, 600)
		self.tabWidget = QTabWidget(self)
		self.tab1 = QWidget(self.tabWidget)
		self.tab1.setEnabled(True)
		self.tabWidget.addTab(self.tab1, 'tab1')
		self.frame1 = QFrame(self.tab1)
		# self.frame1.setGeometry(QtCore.QRect(40, 20, 221, 151))
		self.frame1.setFrameShape(QFrame.StyledPanel)
		self.pushbutton1 = QPushButton(self.frame1)
		# self.pushbutton1.setGeometry(QtCore.QRect(60, 20, 113, 32))
		self.textedit1 = QTextEdit(self.frame1)
		# self.textedit1.setGeometry(QtCore.QRect(60, 60, 104, 79))
		self.frame2 = QFrame(self.tab1)
		# self.frame2.setGeometry(QtCore.QRect(330, 30, 201, 141))
		self.frame2.setFrameShape(QFrame.StyledPanel)
		self.pushbutton2 = QPushButton(self.frame2)
		# self.pushbutton2.setGeometry(QtCore.QRect(50, 20, 113, 32))
		self.textedit2 = QTextEdit(self.frame2)
		# self.textedit2.setGeometry(QtCore.QRect(50, 50, 104, 79))
		self.tab2 = QWidget(self.tabWidget)
		self.tab2.setEnabled(True)
		self.tabWidget.addTab(self.tab2, 'tab2')
		self.tabWidget.setTabText(0, 'tab1')
		self.tabWidget.setTabText(1, 'tab2')
		self.sp1 = QSplitter(Qt.Horizontal)
		self.sp1.addWidget(self.frame1)
		self.sp1.addWidget(self.frame2)
		self.sp1.setSizes([200,400])
		self.setCentralWidget(self.tabWidget)
		self.layout_init()

	def layout_init(self):
		self.v1layout = QVBoxLayout()
		self.h1layout = QHBoxLayout()
		self.h2layout = QHBoxLayout()
		self.v1layout.addWidget(self.pushbutton1)
		self.v1layout.addWidget(self.textedit1)
		self.frame1.setLayout(self.v1layout)
		self.h1layout.addWidget(self.pushbutton2)
		self.h1layout.addWidget(self.textedit2)
		self.frame2.setLayout(self.h1layout)
		self.h2layout.addWidget(self.frame1)
		self.h2layout.addWidget(self.frame2)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	radar_test = Ui_MainWindow()
	radar_test.show()
	sys.exit(app.exec())