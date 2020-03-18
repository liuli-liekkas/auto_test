from PyQt5.QtWidgets import QApplication
import UILogin
import sys

app = QApplication(sys.argv)
Login_in = UILogin.LoginWindow()
Login_in.show()
sys.exit(app.exec_())

