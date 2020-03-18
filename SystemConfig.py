import MachineClass
import UIRadarTest
import time
import winsound
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QThread


class MyThread(QThread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        test = UIRadarTest.RadarTestMain()
        test.show()


app = QApplication(sys.argv)
my_thread = MyThread()
my_thread.run()
while True:
    test_set = UIRadarTest.HorizontalPowerMenu()
    test_result = test_set.min_range_output()
    print(test_result)
    print('1')
    time.sleep(1)


