#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author  : Muzi_Li
File    : landing.py
Time    : 2019-01-08 14:19
Software: PyCharm
'''
from PyQt5.Qt import QWidget, pyqtSignal, QPropertyAnimation, QAbstractAnimation, QPoint
from resource.Landing_ui import Ui_Form


class LandingPanel(QWidget, Ui_Form):
    landing_sig = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_label(self):
        # 设置姓名密码为空
        self.name_le.setText("")
        self.password_le.setText("")

    def btn_sate_le(self):
        # 设置登陆按钮是否可用
        self.name = self.name_le.text()
        self.pd = self.password_le.text()
        if len(self.name) > 0 and len(self.pd) > 0:
            self.landing_btn.setEnabled(True)
        else:
            self.landing_btn.setEnabled(False)

    def show_error(self):
        # 窗体抖动效果
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self)
        animation.setPropertyName(b'pos')
        animation.setKeyValueAt(0, self.pos())
        animation.setKeyValueAt(0.2, self.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.pos())
        animation.setKeyValueAt(0.7, self.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.pos())
        animation.setDuration(100)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def land_btn(self):
        # 把用户名和密码通过型号传递出去
        ls = []
        ls.append(self.name)
        ls.append(self.pd)
        self.landing_sig.emit(ls)


if __name__ == '__main__':
    import sys
    from PyQt5.Qt import QApplication

    app = QApplication(sys.argv)
    win = LandingPanel()
    win.show()
    sys.exit(app.exec_())
