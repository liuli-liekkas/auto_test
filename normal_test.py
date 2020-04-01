import sys
from PyQt5 import QtSql
import ctypes
if __name__ == '__main__':
	db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
	db.setHostName("localhost")
	db.setDatabaseName("mysql")
	db.setUserName("root")
	db.setPassword("ll891119")
	db.setPort(3306)
	db.open()
	print(QtSql.QSqlDatabase.drivers())
