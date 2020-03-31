import sys
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.db = None
        self.db_connect()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')    # 1
        self.db.setDatabaseName('./test.db')             # 2
        if not self.db.open():                           # 3
            QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

    def closeEvent(self, QCloseEvent):                   # 4
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())