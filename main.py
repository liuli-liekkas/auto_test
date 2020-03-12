from PyQt5.QtWidgets import QApplication
import login_ui
import sys

app = QApplication(sys.argv)
Login_in = login_ui.LoginWindow()
Login_in.show()
sys.exit(app.exec_())

