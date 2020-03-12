import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton
import main

USER_PWD = {
    '刘力': 'liuli',
    '薛岩': 'xueyan',
    '裴毓': 'peiyu',
    '张晓蕾': 'zhangxiaolei',
    '申亚飞': 'shenyafei'
}


class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.resize(300, 100)
        self.setWindowTitle('智能传感器室自动化测试系统')
        self.user_label = QLabel('用户名', self)
        self.pwd_label = QLabel('密码', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('登陆', self)
        self.sign_in_button = QPushButton('注册', self)
        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.layout_init()
        self.line_edit_init()
        self.push_button_init()
        self.sign_in_page = SigInPage()

    def layout_init(self):
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.sign_in_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def line_edit_init(self):
        self.user_line.setPlaceholderText('请输入用户名')
        self.pwd_line.setPlaceholderText('请输入密码')
        self.user_line.textChanged.connect(self.check_input_fuc)
        self.pwd_line.textChanged.connect(self.check_input_fuc)

    def check_input_fuc(self):
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    def push_button_init(self):
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_func)
        self.sign_in_button.clicked.connect(self.show_sign_in_page_func)

    def show_sign_in_page_func(self):
        self.sign_in_page.exec_()

    def check_login_func(self):
        self.select_window = main.SelectWindow()
        if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
            QMessageBox.information(self, '信息', '登陆成功！')
            self.close()
            self.select_window.show()
        else:
            QMessageBox.critical(self, '错误', '用户名或密码错误！')
        self.user_line.clear()
        self.pwd_line.clear()


class SigInPage(QDialog):
    def __init__(self):
        super(SigInPage, self).__init__()
        self.sign_in_user_label = QLabel('用户名', self)
        self.sign_in_pwd1_label = QLabel('密码', self)
        self.sign_in_pwd2_label = QLabel('密码', self)
        self.sign_in_user_line = QLineEdit(self)
        self.sign_in_pwd1_line = QLineEdit(self)
        self.sign_in_pwd2_line = QLineEdit(self)
        self.sign_in_button = QPushButton('注册', self)
        self.user_h_layout = QHBoxLayout()
        self.pwd1_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()
        self.layout_init()
        self.line_edit_init()
        self.push_button_init()

    def layout_init(self):
        self.user_h_layout.addWidget(self.sign_in_user_label)
        self.user_h_layout.addWidget(self.sign_in_user_line)
        self.pwd1_h_layout.addWidget(self.sign_in_pwd1_label)
        self.pwd1_h_layout.addWidget(self.sign_in_pwd1_line)
        self.pwd2_h_layout.addWidget(self.sign_in_pwd2_label)
        self.pwd2_h_layout.addWidget(self.sign_in_pwd2_line)
        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd1_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addWidget(self.sign_in_button)
        self.setLayout(self.all_v_layout)

    def line_edit_init(self):
        self.sign_in_user_line.textChanged.connect(self.check_input_func)
        self.sign_in_pwd1_line.textChanged.connect(self.check_input_func)
        self.sign_in_pwd2_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.sign_in_user_line.text() and self.sign_in_pwd1_line.text() and self.sign_in_pwd2_line.text():
            self.sign_in_button.setEnabled(True)
        else:
            self.sign_in_button.setEnabled(False)

    def push_button_init(self):
        self.sign_in_button.setEnabled(False)
        self.sign_in_button.clicked.connect(self.check_sign_in_func)

    def check_sign_in_func(self):
        if self.sign_in_pwd1_line.text() != self.sign_in_pwd2_line.text():
            QMessageBox.critical(self, '错误', '两次输入密码不相同！')
        elif self.sign_in_user_line.text() not in USER_PWD:
            USER_PWD[self.sign_in_user_line.text()] = self.sign_in_pwd1_line.text()
            QMessageBox.information(self, '提示', '注册成功！')
            self.close()
        else:
            QMessageBox.critical(self, '错误', '该用户名已注册！')
        self.sign_in_user_line.clear()
        self.sign_in_pwd1_line.clear()
        self.sign_in_pwd2_line.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())


