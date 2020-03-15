from PyQt5.QtWidgets import QApplication
import ui_login
import sys

app = QApplication(sys.argv)
Login_in = ui_login.LoginWindow()
Login_in.show()
sys.exit(app.exec_())

