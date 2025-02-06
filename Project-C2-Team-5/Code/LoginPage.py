# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_Arabic = QtWidgets.QCheckBox(Form)
        self.checkBox_Arabic.setObjectName("checkBox_Arabic")
        self.gridLayout.addWidget(self.checkBox_Arabic, 8, 0, 1, 1)
        self.label_2023 = QtWidgets.QLabel(Form)
        self.label_2023.setWordWrap(True)
        self.label_2023.setObjectName("label_2023")
        self.gridLayout.addWidget(self.label_2023, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Login_butt_login = QtWidgets.QPushButton(Form)
        self.Login_butt_login.setObjectName("Login_butt_login")
        self.gridLayout.addWidget(self.Login_butt_login, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.Pass_txt_login = QtWidgets.QLineEdit(Form)
        self.Pass_txt_login.setText("")
        self.Pass_txt_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pass_txt_login.setReadOnly(False)
        self.Pass_txt_login.setObjectName("Pass_txt_login")
        self.gridLayout.addWidget(self.Pass_txt_login, 4, 0, 1, 1)
        self.User_txt_login = QtWidgets.QLineEdit(Form)
        self.User_txt_login.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.User_txt_login.setObjectName("User_txt_login")
        self.gridLayout.addWidget(self.User_txt_login, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 7, 0, 1, 1)
        self.Dark_mode_checkBox = QtWidgets.QCheckBox(Form)
        self.Dark_mode_checkBox.setObjectName("Dark_mode_checkBox")
        self.gridLayout.addWidget(self.Dark_mode_checkBox, 9, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.User_txt_login, self.Pass_txt_login)
        Form.setTabOrder(self.Pass_txt_login, self.Login_butt_login)
        Form.setTabOrder(self.Login_butt_login, self.checkBox_Arabic)
        Form.setTabOrder(self.checkBox_Arabic, self.Dark_mode_checkBox)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox_Arabic.setText(_translate("Form", "Arabic Languge"))
        self.label_2023.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Login</span></p></body></html>"))
        self.Login_butt_login.setText(_translate("Form", "Login"))
        self.Pass_txt_login.setPlaceholderText(_translate("Form", "Password"))
        self.User_txt_login.setPlaceholderText(_translate("Form", "User Name"))
        self.Dark_mode_checkBox.setText(_translate("Form", "Dark Mode"))


class LoginPage (QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self = self.setupUi(self)

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
