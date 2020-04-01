import sys
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Database(QWidget):
	def __init__(self):
		super(Database, self).__init__()
		self.db = None
		self.db_connect()

	def db_connect(self):
		self.db = QSqlDatabase.addDatabase('QMYSQL')
		self.db.setHostName('localhost')
		self.db.setDatabaseName('test')
		self.db.setUserName('root')
		self.db.setPassword('ll891119')
		if not self.db.open():
			QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

	def closeEvent(self, QCloseEvent):
		self.db.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	database = Database()
	database.show()
	sys.exit(app.exec_())
