#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author  : Muzi_Li
File    : Link_MySQL.py
Time    : 2019-01-11 9:48
Software: PyCharm
'''
import pymysql


class LinkMySQL(object):
    def __init__(self):
        self.conn = pymysql.connect(host='129.204.92.221',  # ID地址
                                    port=3308,  # 端口号
                                    user='price',  # 用户名
                                    passwd='123456',  # 密码
                                    database='job_log',  # 库名
                                    charset='utf8')  # 链接字符集
        self.cur = self.conn.cursor()

    def select_user(self, ls):
        sql = "SELECT * FROM user WHERE 姓名 = %s"
        return self.select_sql(sql, ls)

    def commit_sql(self, sql, ls, num=True):
        """
        执行增删改语句，num=True，单条执行,num=False，批量操作
        :param sql:
        :param ls:
        :return: 返回执行的结果, 1 = 成功, 0 = 失败
        """
        try:
            if num:
                self.cur.execute(sql, ls)
            else:
                self.cur.executemany(sql, ls)
            self.conn.commit()
            return 1
        except Exception as e:
            self.conn.rollback()
            return 0
        finally:
            self.cur.close()
            self.conn.close()

    def select_sql(self, sql, ls):
        """
        执行有条件的查询语句
        :param sql:查询SQL语句
        :param ls: SQL语句占位集合
        :return: 返回查询得到的数据集
        """
        self.cur.execute(sql, ls)
        data = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return data

    def select_single(self, sql, type=1):
        """
        执行没有条件的查询语句 type 1 = 数据 , 0 = 列
        :param sql:查询SQL语句
        :param ls: SQL语句占位集合
        :return: 返回查询得到的数据集
        """
        self.cur.execute(sql)
        if type:
            data = self.cur.fetchall()
        else:
            data = self.cur.description
        self.cur.close()
        self.conn.close()
        return data


if __name__ == '__main__':
    name = "姓名"
    link = LinkMySQL()
    data = link.select_temporary(name)
    print(data)
