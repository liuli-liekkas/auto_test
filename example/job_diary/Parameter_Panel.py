#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-12 16:29
# @Author  : Muzi_Li
# @File    : Parameter_Panel.py
# @Software: PyCharm

from PyQt5.Qt import QWidget, QInputDialog, QLineEdit, QMessageBox
from Link_MySQL import LinkMySQL
from resource.Parameter_ui import Ui_Form


class ParameterPanel(QWidget, Ui_Form):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        self.name = name

    def set_list(self, sort):
        # 点击左侧，右侧显示数据
        self.sort = sort
        sql_parameter = "SELECT 小类 FROM parameter WHERE 姓名 = %s AND 大类 = %s ORDER BY 排序"
        ls = []
        ls.append(self.name)
        ls.append(sort)
        data = LinkMySQL().select_sql(sql_parameter, ls)
        self.listWidget.clear()  # 清空右侧的List
        self.listWidget.addItems([x[0] for x in data])  # 重新给右侧的List添加数据

    def add_list(self):
        # 新增右侧数据
        text, okPressed = QInputDialog.getText(self, "新增", "请输入内容", QLineEdit.Normal, "")
        if okPressed and text != '':
            r = self.listWidget.currentRow()
            if r == -1:  # 如果没有选中右侧的条目，则在第一行新增
                self.listWidget.insertItem(0, text)
                self.listWidget.setCurrentRow(0)
            else:  # 如果选中了右侧的条目，则在选中的条目下方新增
                self.listWidget.insertItem(r + 1, text)
                self.listWidget.setCurrentRow(r + 1)  # 选中新增的行

    def clear_list(self):
        # 删除右侧
        r = self.listWidget.currentRow()
        if r > -1:
            ls = []
            ls.append(self.name)
            ls.append(self.sort)
            ls.append(self.listWidget.currentItem().text())
            self.listWidget.takeItem(r)  # 删除列表元素

    def up(self):
        # 向上移动
        r = self.listWidget.currentRow()
        if r > -1:
            t = self.listWidget.currentItem().text()
            if r - 1 > -1:
                self.listWidget.takeItem(r)  # 删除列表元素
                self.listWidget.insertItem(r - 1, t)
                self.listWidget.setCurrentRow(r - 1)

    def down(self):
        # 向下移动
        r = self.listWidget.currentRow()
        if r > -1:
            t = self.listWidget.currentItem().text()
            if r + 1 < self.listWidget.count():
                self.listWidget.takeItem(r)  # 删除列表元素
                self.listWidget.insertItem(r + 1, t)
                self.listWidget.setCurrentRow(r + 1)

    def ok(self):
        # 先删除
        sql = "DELETE FROM parameter WHERE 姓名=%s and 大类=%s"
        ls = []
        ls.append(self.name)
        ls.append(self.sort)
        LinkMySQL().commit_sql(sql, ls)
        # 后新增
        ls = []
        tup = []
        for r in range(self.listWidget.count()):
            tup.append(self.name)
            tup.append(self.sort)
            tup.append(self.listWidget.item(r).text())
            tup.append(r)
            tup = tuple(tup)
            ls.append(tup)
            tup = []
        sql = "INSERT INTO parameter values (%s,%s,%s,%s)"
        LinkMySQL().commit_sql(sql, ls, num=False)
        QMessageBox.information(self,
                                "温馨提示",
                                "修改成功",
                                QMessageBox.Yes)


if __name__ == '__main__':
    import sys
    from PyQt5.Qt import QApplication, QListWidget

    app = QApplication(sys.argv)
    name = '张三'
    win = ParameterPanel(name)

    win.show()
    sys.exit(app.exec_())
