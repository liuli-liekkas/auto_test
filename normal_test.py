import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QComboBox,QFrame

class MyClass(QWidget):
    def __init__(self):
        super(MyClass, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("刘金玉编程")
        self.setGeometry(300,100,400,300)

        myframe1=QFrame(self)
        myframe1.move(50,50)
        lbl1=QLabel("省",myframe1)
        lbl1.move(0,3)
        combo1=QComboBox(myframe1)
        combo1.move(20,0)
        # combo1.setEditable(True)

        combo1.activated[str].connect(self.myActived)

        #省份
        combo1.addItem("选择省份")
        combo1.addItem("浙江")
        combo1.addItem("江苏")
        combo1.addItem("安徽")

        #市级
        lbl1 = QLabel("市", myframe1)
        lbl1.move(100, 3)
        self.combo2 = QComboBox(myframe1)
        self.combo2.move(120, 0)

        self.show()

    def myActived(self,s):
        self.combo2.clear()
        if s=="浙江":
            self.combo2.addItem("杭州")
            self.combo2.addItem("宁波")
            self.combo2.addItem("温州")
        elif s=="江苏":
            self.combo2.addItem("苏州")
            self.combo2.addItem("无锡")
            self.combo2.addItem("扬州")
            self.combo2.addItem("南京")


if __name__=="__main__":
    app=QApplication(sys.argv)
    mc=MyClass()
    app.exec_()