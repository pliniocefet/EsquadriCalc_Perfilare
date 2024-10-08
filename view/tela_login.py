# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from telas_ui import files_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 477)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(300, 460))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 4, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_bar)
        self.frame_error.setMaximumSize(QtCore.QSize(300, 40))
        self.frame_error.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                       "border-radius: 7px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.pushButton_error = QtWidgets.QPushButton(self.frame_error)
        self.pushButton_error.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_error.setStyleSheet("QPushButton {\n"
                                            "    border-radius: 5px;\n"
                                            "    background-image: url(:/Close_image/cil-x.png);\n"
                                            "    background-position: center;\n"
                                            "    background-color: rgb(100, 100, 100);\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(50, 50, 50);\n"
                                            "    color: rgb(200, 200, 200);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    color: rgb(200, 200, 200);\n"
                                            "}")
        self.pushButton_error.setText("")
        self.pushButton_error.setObjectName("pushButton_error")
        self.horizontalLayout_3.addWidget(self.pushButton_error)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(300, 550))
        self.login_area.setStyleSheet("border-radius: 10px")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.logo = QtWidgets.QFrame(self.login_area)
        self.logo.setGeometry(QtCore.QRect(35, 18, 230, 80))
        self.logo.setStyleSheet("background-image: url(:/logon/Esquadricalc-230x80.png);\n"
                                "background-repeat: no-repeat;\n"
                                "background-position: center;")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.frame_avatar = QtWidgets.QFrame(self.login_area)
        self.frame_avatar.setGeometry(QtCore.QRect(105, 110, 90, 90))
        self.frame_avatar.setStyleSheet("QFrame {\n"
                                        "    background-image: url(:/Avatar/avatar_login.png);\n"
                                        "    background-image: url(:/Avatar/avatar_login.png);\n"
                                        "    background-position: center;\n"
                                        "    border-radius: 45px;\n"
                                        "    border: 7px solid rgb(255, 255, 0);\n"
                                        "}\n"
                                        "QFrame:hover {\n"
                                        "    border: 7px solid rgb(255, 200, 0);\n"
                                        "}")
        self.frame_avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_avatar.setObjectName("frame_avatar")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_user.setGeometry(QtCore.QRect(65, 208, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet("QLineEdit {\n"
                                         "    border-radius: 7px;\n"
                                         "    border: 2px solid rgb(40, 40, 40);\n"
                                         "    padding: 7px;\n"
                                         "    background-color: rgb(20, 20, 20);\n"
                                         "    color:rgb(237, 237, 4);\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(60, 60, 60);\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit:focus {\n"
                                         "    background-color: rgb(150, 150, 150);\n"
                                         "    border: 2px solid rgb(255, 255, 0);\n"
                                         "}")
        self.lineEdit_user.setMaxLength(12)
        self.lineEdit_user.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_password.setGeometry(QtCore.QRect(65, 250, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
                                             "    border-radius: 7px;\n"
                                             "    border: 2px solid rgb(40, 40, 40);\n"
                                             "    padding: 7px;\n"
                                             "    background-color: rgb(20, 20, 20);\n"
                                             "    color: rgb(255, 255, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 2px solid rgb(60, 60, 60);\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus {\n"
                                             "    border: 2px solid rgb(255, 255, 0);\n"
                                             "    background-color: rgb(150, 150, 150);\n"
                                             "}\n"
                                             "")
        self.lineEdit_password.setMaxLength(8)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.checkBox_save_user = QtWidgets.QCheckBox(self.login_area)
        self.checkBox_save_user.setGeometry(QtCore.QRect(65, 294, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.checkBox_save_user.setFont(font)
        self.checkBox_save_user.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox_save_user.setStyleSheet("QCheckBox::indicator {\n"
                                              "    border-radius: 6px;\n"
                                              "    border: 2px solid rgb(255, 255, 0);\n"
                                              "    width: 10px;\n"
                                              "    height: 10px;\n"
                                              "    background-color: rgb(135, 135, 135)\n"
                                              "}\n"
                                              "QCheckBox::indicator:checked {\n"
                                              "    background-color: rgb(255, 255, 0);\n"
                                              "    border: 2px solid rgb(255, 255, 0);\n"
                                              "}")
        self.checkBox_save_user.setTristate(False)
        self.checkBox_save_user.setObjectName("checkBox_save_user")
        self.pushButton_login = QtWidgets.QPushButton(self.login_area)
        self.pushButton_login.setGeometry(QtCore.QRect(60, 330, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton {\n"
                                            "    border: 2px solid rgb(60, 60, 60);\n"
                                            "    background-color: rgb(50, 50, 50);\n"
                                            "    border-radius: 5px;\n"
                                            "    \n"
                                            "    color: rgb(255, 255, 0);\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    border: 2px solid rgb(70, 70, 70);\n"
                                            "    background-color: rgb(60, 60, 60);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(20, 20, 20);\n"
                                            "    border: 2px solid rgb(255, 255, 0);\n"
                                            "}")
        self.pushButton_login.setFlat(False)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.botton = QtWidgets.QFrame(self.centralwidget)
        self.botton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.botton.setStyleSheet("background-color: rgb(20, 20, 20);")
        self.botton.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.botton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botton.setObjectName("botton")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.botton)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_credits = QtWidgets.QLabel(self.botton)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(80, 80, 80);")
        self.label_credits.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_2.addWidget(self.label_credits)
        self.verticalLayout.addWidget(self.botton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_error.setText(_translate("MainWindow", "Error"))
        self.lineEdit_user.setPlaceholderText(
            _translate("MainWindow", "Usuario"))
        self.lineEdit_password.setPlaceholderText(
            _translate("MainWindow", "Senha"))
        self.checkBox_save_user.setText(_translate("MainWindow", "Save Login"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.label_credits.setText(_translate(
            "MainWindow", "Created By: Plinio Corrêa"))
