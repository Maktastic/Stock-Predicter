from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
import time
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
import datetime
from login import Login
class Signup(QtWidgets.QWidget):
        def __init__(self):
                super(Signup, self).__init__()
                self.setupUi(self)
        def setupUi(self, Signup):
                Signup.setObjectName("Signup")
                Signup.resize(398, 734)
                font = QtGui.QFont()
                font.setPointSize(15)
                Signup.setFont(font)
                self.frame = QtWidgets.QFrame(Signup)
                self.frame.setGeometry(QtCore.QRect(0, 0, 400, 800))
                font = QtGui.QFont()
                font.setPointSize(4)
                self.frame.setFont(font)
                self.frame.setStyleSheet("QFrame\n"
                "{\n"
                "background: #333;\n"
                "}")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.edit_username = QtWidgets.QLineEdit(self.frame)
                self.edit_username.setGeometry(QtCore.QRect(70, 109, 270, 30))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.edit_username.setFont(font)
                self.edit_username.setStyleSheet("")
                self.edit_username.setObjectName("edit_username")
                self.edit_password = QtWidgets.QLineEdit(self.frame)
                self.edit_password.setGeometry(QtCore.QRect(70, 237, 270, 30))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.edit_password.setFont(font)
                self.edit_password.setObjectName("edit_password")
                self.label_error = QtWidgets.QLabel(self.frame)
                self.label_error.setGeometry(QtCore.QRect(70, 681, 270, 30))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(8)
                self.label_error.setFont(font)
                self.label_error.setFocusPolicy(QtCore.Qt.NoFocus)
                self.label_error.setStyleSheet("QLabel#label_error\n"
                "{\n"
                "    color: white;\n"
                "}")
                self.label_error.setAlignment(QtCore.Qt.AlignCenter)
                self.label_error.setObjectName("label_error")
                self.submit_login = QtWidgets.QPushButton(self.frame)
                self.submit_login.setGeometry(QtCore.QRect(240, 618, 100, 40))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.submit_login.setFont(font)
                self.submit_login.setStyleSheet("QPushButton#submit_login\n"
                "{\n"
                "    position: relative;\n"
                "      padding: 0;\n"
                "    border-width: 0;\n"
                "      outline: none;\n"
                "      border-radius: 2px;\n"
                "      background-color: red;\n"
                "      color: #ecf0f1;\n"
                "}\n"
                "\n"
                "")
                self.submit_login.setObjectName("submit_login")
                self.password_btn = QtWidgets.QPushButton(self.frame)
                self.password_btn.setGeometry(QtCore.QRect(0, 166, 400, 50))
                font = QtGui.QFont()
                font.setPointSize(7)
                self.password_btn.setFont(font)
                self.password_btn.setStyleSheet("QPushButton#password_btn\n"
                "{\n"
                "    background:red;\n"
                "    border-radius: 60px;\n"
                "}\n"
                "")
                self.password_btn.setText("")
                icon = QtGui.QIcon()
                r_path = 'Designs/Images/password_btn.png'
                c_dir = os.getcwd()
                p = os.path.join(c_dir, r_path)
                icon.addPixmap(QtGui.QPixmap(p), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.password_btn.setIcon(icon)
                self.password_btn.setObjectName("password_btn")
                self.username_btn = QtWidgets.QPushButton(self.frame)
                self.username_btn.setGeometry(QtCore.QRect(0, 37, 400, 50))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(10)
                font.setKerning(True)
                self.username_btn.setFont(font)
                self.username_btn.setStyleSheet("QPushButton#username_btn\n"
                "{\n"
                "    background:red;\n"
                "    border-radius: 60px;\n"
                "}")
                self.username_btn.setText("")
                icon1 = QtGui.QIcon()
                r_path = 'Designs/Images/top_login.png'
                c_dir = os.getcwd()
                u = os.path.join(c_dir, r_path)
                icon1.addPixmap(QtGui.QPixmap(u), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.username_btn.setIcon(icon1)
                self.username_btn.setFlat(True)
                self.username_btn.setObjectName("username_btn")
                self.firstname_btn = QtWidgets.QPushButton(self.frame)
                self.firstname_btn.setGeometry(QtCore.QRect(0, 290, 400, 50))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(10)
                self.firstname_btn.setFont(font)
                self.firstname_btn.setStyleSheet("QPushButton#firstname_btn\n"
                "{\n"
                "    background:red;\n"
                "    border-radius: 60px;\n"
                "    color: #ffebee;\n"
                "}\n"
                "")
                self.firstname_btn.setObjectName("firstname_btn")
                self.edit_firstname = QtWidgets.QLineEdit(self.frame)
                self.edit_firstname.setGeometry(QtCore.QRect(70, 361, 270, 30))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.edit_firstname.setFont(font)
                self.edit_firstname.setObjectName("edit_firstname")
                self.dob_btn = QtWidgets.QPushButton(self.frame)
                self.dob_btn.setGeometry(QtCore.QRect(0, 410, 400, 50))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(10)
                self.dob_btn.setFont(font)
                self.dob_btn.setStyleSheet("QPushButton#dob_btn\n"
                "{\n"
                "    background:red;\n"
                "    border-radius: 60px;\n"
                "    color: #ffebee;\n"
                "}\n"
                "")
                self.dob_btn.setObjectName("dob_btn")
                self.edit_dob = QtWidgets.QLineEdit(self.frame)
                self.edit_dob.setGeometry(QtCore.QRect(70, 490, 270, 30))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                self.edit_dob.setFont(font)
                self.edit_dob.setObjectName("edit_dob")

                Signup.setWindowTitle("Signup Portal")
                self.submit_login.setText("Signup")
                self.firstname_btn.setText("Full Name")
                self.dob_btn.setText("Date Of Birth (dd/mm/yyyy)")

                #BUTTON EVENTS
                self.submit_login.clicked.connect(self.signup)
                QtCore.QMetaObject.connectSlotsByName(Signup)
        def signup(self):
                found = 0
                username = self.edit_username.text()
                while found == 0:
                        username = self.edit_username.text()
                        try:
                                con = sql.connect('users.db')
                                cursor = con.cursor()
                                finduser = "SELECT * FROM users WHERE username = ?"
                                cursor.execute(finduser, [(username)])
                                if cursor.fetchall():
                                        self.label_error.setText("Username has already been taken!")
                                        self.edit_username.clear()
                                        QApplication.processEvents()
                                        break
                                else:
                                        found = 1
                                        break
                        except sql.Error as e:
                                self.label_error.setText(f"{e}")
                                QApplication.processEvents()

                name = self.edit_firstname.text()
                password = self.edit_password.text()
                dob = self.edit_dob.text()
                day, month, year = dob.split('/')
                isValidDate = True
                try:
                        datetime.datetime(int (year), int (month), int (day))
                except ValueError:
                        isValidDate = False
                
                if not isValidDate:
                        self.label_error.setText('Birth of Date is typed incorrectly')
                        QApplication.processEvents()
                
                insert_data = '''INSERT INTO users(username, password, name, dob) VALUES (?,?,?,?)'''
                cursor.execute(insert_data, [(username), (password), (name), (dob)])
                con.commit()
                self.label_error.setText("User has been created")
                self.hide()
                QApplication.processEvents()
                self.window = QtWidgets.QMainWindow()
                self.ui = Login()
                self.ui.setupUi(self.window)
                self.window.show()
                QApplication.processEvents()

                


                
