#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-15 下午 09:42
# @Author  : Muzi_Li
# @File    : Joblog_Panel.py
# @Software: PyCharm

from PyQt5.Qt import QWidget, QDate, QTableWidgetItem
from resource.Joblog_ui import Ui_Form
from Link_MySQL import LinkMySQL
from Query_Panel import QueryPanel
from Parameter_Panel import ParameterPanel


class JoblogPanel(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.setColumnWidth(9, 0)
        self.dateEdit.setDate(QDate.currentDate())  # 设置日期为当天
        self.id = ""

    def show_detail(self, r):
        """
        选中table行后，显示数据明细
        :param r: 选中的行号
        :return:
        """
        self.dateEdit.setDate(QDate.fromString(self.tableWidget.item(r.row(), 0).text(), 1))  # 时间
        self.comboBox.setCurrentText(self.tableWidget.item(r.row(), 1).text())  # 工作分类
        self.textEdit.setPlainText(self.tableWidget.item(r.row(), 2).text())  # 事项内容
        self.comboBox_2.setCurrentText(self.tableWidget.item(r.row(), 3).text())  # 工时
        self.comboBox_3.setCurrentText(self.tableWidget.item(r.row(), 4).text())  # 性质
        self.comboBox_4.setCurrentText(self.tableWidget.item(r.row(), 5).text())  # 重要等级
        self.comboBox_5.setCurrentText(self.tableWidget.item(r.row(), 6).text())  # 状态
        self.comboBox_6.setCurrentText(self.tableWidget.item(r.row(), 7).text())  # 工作配合
        self.textEdit_2.setPlainText(self.tableWidget.item(r.row(), 8).text())  # 问题和困难
        self.id = self.tableWidget.item(r.row(), 9).text()

    def get_list(self):
        # 获取文本框的信息
        ls = []
        ls.append(self.lineEdit.text())  # 姓名
        ls.append(self.lineEdit_2.text())  # 部门
        ls.append(self.lineEdit_3.text())  # 岗位
        ls.append(self.dateEdit.text())  # 时间
        ls.append(self.comboBox.currentText())  # 工作分类
        ls.append(self.textEdit.toPlainText())  # 事项内容
        ls.append(self.comboBox_2.currentText())  # 工时
        ls.append(self.comboBox_3.currentText())  # 性质
        ls.append(self.comboBox_4.currentText())  # 重要等级
        ls.append(self.comboBox_5.currentText())  # 状态
        ls.append(self.comboBox_6.currentText())  # 工作配合
        ls.append(self.textEdit_2.toPlainText())  # 问题和困难
        return ls

    def update_table(self):
        # 更新数据，并显示在table
        sql = "SELECT 时间, 工作分类, 事项内容,工时,性质,重要等级,状态," \
              "工作配合,问题和困难, temprary_id FROM temporary WHERE 姓名 = %s"
        data = LinkMySQL().select_sql(sql, self.name)
        self.tableWidget.setRowCount(len(data))
        for c, lindata in enumerate(data):
            for r, value in enumerate(lindata):
                it = QTableWidgetItem(str(value))
                self.tableWidget.setItem(c, r, it)

    def get_users(self, user):
        # 设置参数
        self.user = user
        self.name = user[0]
        self.lineEdit.setText(user[0])
        self.lineEdit_2.setText(user[1])
        self.lineEdit_3.setText(user[2])
        self.update_table()  # 更新表数据
        # 工作分类
        sql_parameter = "SELECT 小类 FROM parameter WHERE 姓名 = %s AND 大类 = '工作分类' ORDER BY 排序"
        data = LinkMySQL().select_sql(sql_parameter, self.name)
        for value in data:
            self.comboBox.addItem(value[0])

        # 工时
        sql_parameter = "SELECT 小类 FROM parameter WHERE 姓名 = %s AND 大类 = '工时' ORDER BY 排序"
        data = LinkMySQL().select_sql(sql_parameter, self.name)
        for value in data:
            self.comboBox_2.addItem(value[0])

        # 性质
        sql_parameter = "SELECT 小类 FROM parameter WHERE 姓名 = %s AND 大类 = '性质' ORDER BY 排序"
        data = LinkMySQL().select_sql(sql_parameter, self.name)
        for value in data:
            self.comboBox_3.addItem(value[0])

        # 重要程度
        sql_parameter = "SELECT 小类 FROM parameter WHERE 姓名 = %s AND 大类 = '重要程度' ORDER BY 排序"
        data = LinkMySQL().select_sql(sql_parameter, self.name)
        for value in data:
            self.comboBox_4.addItem(value[0])

        # 状态
        sql_parameter = "SELECT 小类 FROM parameter WHERE 姓名 = %s AND 大类 = '状态' ORDER BY 排序"
        data = LinkMySQL().select_sql(sql_parameter, self.name)
        for value in data:
            self.comboBox_5.addItem(value[0])

        # 工作配合
        sql_parameter = "SELECT 小类 FROM parameter WHERE 姓名 = %s AND 大类 = '工作配合' ORDER BY 排序"
        data = LinkMySQL().select_sql(sql_parameter, self.name)
        for value in data:
            self.comboBox_6.addItem(value[0])

    def insert_temporary(self):
        # 保存按钮
        ls = self.get_list()
        sql = "INSERT INTO temporary(姓名,部门,岗位,时间,工作分类,事项内容,工时,性质,重要等级,状态,工作配合,问题和困难) " \
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        LinkMySQL().commit_sql(sql, ls)
        self.update_table()  # 更新表数据

    def update_tamporary(self):
        # 修改按钮
        if len(self.id) > 0:
            sql = "UPDATE temporary SET 姓名=%s,部门=%s,岗位=%s,时间=%s,工作分类=%s,事项内容=%s," \
                  "工时=%s,性质=%s,重要等级=%s,状态=%s,工作配合=%s,问题和困难=%s WHERE temprary_id = %s"
            ls = self.get_list()
            ls.append(self.id)
            LinkMySQL().commit_sql(sql, ls)
            self.update_table()  # 更新表数据

    def delete_tamporary(self):
        # 删除按钮
        if len(self.id) > 0:
            sql = "DELETE FROM temporary WHERE temprary_id = %s"
            LinkMySQL().commit_sql(sql, self.id)
            self.update_table()  # 更新表数据

    def insert_log(self):
        # 提交按钮
        if self.tableWidget.rowCount() > 0:
            sql_temporary = "SELECT * FROM temporary WHERE 姓名 = %s"
            data = LinkMySQL().select_sql(sql_temporary, self.name)
            sql_log = "INSERT INTO log(temprary_id,姓名,部门,岗位,时间,工作分类,事项内容,工时,性质,重要等级,状态," \
                      "工作配合,问题和困难) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            LinkMySQL().commit_sql(sql_log, data, False)
            delete_sql = "DELETE FROM temporary WHERE 姓名 = %s"
            LinkMySQL().commit_sql(delete_sql, self.name)
            self.update_table()

    def show_query(self):
        # 查询按钮
        self.query = QueryPanel(self.user)
        self.query.show()

    def show_parameter(self):
        # 配置按钮
        self.parameter = ParameterPanel(self.name)
        self.parameter.show()


if __name__ == '__main__':
    import sys
    from PyQt5.Qt import QApplication

    app = QApplication(sys.argv)
    win = JoblogPanel()
    user = ('张三', '市场部', '经理', '123')
    win.get_users(user)
    win.show()
    sys.exit(app.exec_())
