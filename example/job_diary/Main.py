#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author  : Muzi_Li
File    : Main.py
Time    : 2019-01-11 9:46
Software: PyCharm
'''

from PyQt5.Qt import QApplication
from Landing_Panel import LandingPanel
from Joblog_Panel import JoblogPanel
from Link_MySQL import LinkMySQL
import sys

app = QApplication(sys.argv)
landing = LandingPanel()
joblog = JoblogPanel()


def show_joblog(ls):
    """
    验证用户信息
    :param ls: 获取用户的密码和姓名
    :return:
    """
    users = LinkMySQL().select_user(ls[0])
    if len(users) == 0 or ls[1] != users[0][3]:
        landing.show_error()
    else:
        landing.hide()
        joblog.get_users(users[0])
        joblog.show()


landing.landing_sig.connect(show_joblog)  # 登陆按钮信号

landing.show()
sys.exit(app.exec_())
