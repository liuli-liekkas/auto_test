#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-16 11:33
# @Author  : Muzi_Li
# @File    : Query_Panel.py
# @Software: PyCharm

from PyQt5.Qt import QWidget, QTableWidgetItem, QMessageBox
from resource.Query_ui import Ui_Form
from Link_MySQL import LinkMySQL
import csv
import datetime


class QueryPanel(QWidget, Ui_Form):
    def __init__(self, user):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.clearContents()  # 清除表数据
        self.user = user
        self.data = ''

    def query_detail(self):
        # 查询按钮
        sql = "SELECT 部门 FROM power WHERE 姓名 = %s"
        self.data = LinkMySQL().select_sql(sql, self.user[0])
        ls = []
        ls.append(self.user[0])
        ls.append(self.dateEdit.text())
        ls.append(self.dateEdit_2.text())
        if len(self.data) > 0:
            sql = "SELECT 姓名,部门,岗位,时间,工作分类,事项内容,工时,性质,重要等级,状态,工作配合,问题和困难 FROM log " \
                  "WHERE 姓名 IN( " \
                  "SELECT 姓名 FROM user WHERE 部门 IN( SELECT 部门 FROM power WHERE 姓名 = %s)) " \
                  "AND DATE(时间) >= %s AND DATE(时间) <= %s OR 姓名 = %s"
            ls.append(self.user[0])
        else:
            sql = "SELECT 姓名,部门,岗位,时间,工作分类,事项内容,工时,性质,重要等级,状态,工作配合,问题和困难 FROM log " \
                  "WHERE 姓名 = %s AND DATE(时间) >= %s AND DATE(时间) <= %s"

        self.data = LinkMySQL().select_sql(sql, ls)  # 执行SQL语句
        # 将查询得到的数据显示在Table
        self.tableWidget.setRowCount(len(self.data))
        for c, lindata in enumerate(self.data):
            for r, value in enumerate(lindata):
                it = QTableWidgetItem(str(value))
                self.tableWidget.setItem(c, r, it)

    def derived_table(self):
        # 导出按钮
        if len(self.data) > 0:
            column = ["姓名", "部门", "岗位", "时间", "工作分类", "事项内容", "工时",
                      "性质", "重要等级", "状态", "工作配合", "问题和困难"]
            now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            work_name = self.user[0] + now + ".csv"
            csvfile = open(work_name, 'w', newline='')
            writer = csv.writer(csvfile)
            writer.writerow(column)
            writer.writerows(list(self.data))
            csvfile.close()
            QMessageBox.information(self, "温馨提示", "导出成功", QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    from PyQt5.Qt import QApplication

    app = QApplication(sys.argv)
    user = ('张三', '市场部', '经理', '123')
    win = QueryPanel(user)
    win.show()
    sys.exit(app.exec_())
