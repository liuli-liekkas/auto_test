# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Joblog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1008, 646)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_6)
        self.widget_3.setObjectName("widget_3")
        self.formLayout = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dateEdit = QtWidgets.QDateEdit(self.widget_3)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2019, 1, 15))
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_5.setObjectName("comboBox_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_5)
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_6)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_6)
        self.widget_4.setObjectName("widget_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.textEdit = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit.setObjectName("textEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout_3.addWidget(self.widget)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.insert_temporary)
        self.pushButton.clicked.connect(Form.insert_log)
        self.tableWidget.clicked['QModelIndex'].connect(Form.show_detail)
        self.pushButton_4.clicked.connect(Form.delete_tamporary)
        self.pushButton_5.clicked.connect(Form.update_tamporary)
        self.pushButton_6.clicked.connect(Form.show_query)
        self.pushButton_3.clicked.connect(Form.show_parameter)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.dateEdit, self.comboBox)
        Form.setTabOrder(self.comboBox, self.comboBox_2)
        Form.setTabOrder(self.comboBox_2, self.comboBox_3)
        Form.setTabOrder(self.comboBox_3, self.comboBox_4)
        Form.setTabOrder(self.comboBox_4, self.comboBox_5)
        Form.setTabOrder(self.comboBox_5, self.comboBox_6)
        Form.setTabOrder(self.comboBox_6, self.textEdit)
        Form.setTabOrder(self.textEdit, self.textEdit_2)
        Form.setTabOrder(self.textEdit_2, self.tableWidget)
        Form.setTabOrder(self.tableWidget, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Form.setTabOrder(self.lineEdit_3, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "姓名"))
        self.label.setText(_translate("Form", "部门"))
        self.label_2.setText(_translate("Form", "岗位"))
        self.label_4.setText(_translate("Form", "时间"))
        self.label_5.setText(_translate("Form", "工作分类"))
        self.label_7.setText(_translate("Form", "工时"))
        self.label_8.setText(_translate("Form", "性质"))
        self.label_9.setText(_translate("Form", "重要/紧急"))
        self.label_10.setText(_translate("Form", "状态"))
        self.label_11.setText(_translate("Form", "工作配合"))
        self.label_6.setText(_translate("Form", "事项内容"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_12.setText(_translate("Form", "问题和困难"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "保存"))
        self.pushButton_5.setText(_translate("Form", "修改"))
        self.pushButton_4.setText(_translate("Form", "删除"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.pushButton_6.setText(_translate("Form", "查询"))
        self.pushButton_3.setText(_translate("Form", "配置"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "工作分类"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "事项内容"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "工时"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "性质"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "重要/紧急"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "状态"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "工作配合"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "问题和困难"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
