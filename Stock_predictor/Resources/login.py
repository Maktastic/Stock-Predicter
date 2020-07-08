import sqlite3 as sql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, os
import time
from main import *
from signup import *

class Login(QMainWindow):

        def __init__(self):
                QApplication.__init__(self)
                self.setupUi(self)
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(400, 500)
                MainWindow.setStyleSheet("")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(0, 0, 400, 500))
                font = QtGui.QFont()
                font.setPointSize(10)
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
                font.setPointSize(10)
                self.edit_username.setFont(font)
                self.edit_username.setStyleSheet("")
                self.edit_username.setObjectName("edit_username")
                self.edit_password = QtWidgets.QLineEdit(self.frame)
                self.edit_password.setGeometry(QtCore.QRect(70, 237, 270, 30))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(10)
                self.edit_password.setFont(font)
                self.edit_password.setObjectName("edit_password")
                self.label_error = QtWidgets.QLabel(self.frame)
                self.label_error.setGeometry(QtCore.QRect(70, 360, 270, 30))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(10)
                self.label_error.setFont(font)
                self.label_error.setFocusPolicy(QtCore.Qt.NoFocus)
                self.label_error.setStyleSheet("QLabel#label_error\n"
                "{\n"
                "    color: white;\n"
                "}")
                self.label_error.setAlignment(QtCore.Qt.AlignCenter)
                self.label_error.setObjectName("label_error")
                self.submit_login = QtWidgets.QPushButton(self.frame)
                self.submit_login.setGeometry(QtCore.QRect(240, 298, 100, 40))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(10)
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
                self.label_needacc = QtWidgets.QLabel(self.frame)
                self.label_needacc.setGeometry(QtCore.QRect(70, 420, 121, 30))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(10)
                self.label_needacc.setFont(font)
                self.label_needacc.setAutoFillBackground(False)
                self.label_needacc.setStyleSheet("QLabel#label_needacc\n"
                "{\n"
                "    color: white;\n"
                "}")
                self.label_needacc.setAlignment(QtCore.Qt.AlignCenter)
                self.label_needacc.setObjectName("label_needacc")
                self.signup_btn = QtWidgets.QPushButton(self.frame)
                self.signup_btn.setGeometry(QtCore.QRect(250, 420, 93, 30))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.signup_btn.setFont(font)
                self.signup_btn.setStyleSheet("QPushButton#signup_btn\n"
                "{\n"
                "    position: relative;\n"
                "      padding: 0;\n"
                "      border-width: 0;\n"
                "      outline: none;\n"
                "      border-radius: 2px;\n"
                "      background-color: red;\n"
                "      color: #ecf0f1;\n"
                "}")
                self.signup_btn.setObjectName("signup_btn")
                self.password_btn = QtWidgets.QPushButton(self.frame)
                self.password_btn.setGeometry(QtCore.QRect(0, 166, 400, 50))
                font = QtGui.QFont()
                font.setPointSize(10)
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
                u = os.path.join(c_dir, r_path)
                icon.addPixmap(QtGui.QPixmap(u), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
                p = os.path.join(c_dir, r_path)
                icon1.addPixmap(QtGui.QPixmap(p), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.username_btn.setIcon(icon1)
                self.username_btn.setFlat(True)
                self.username_btn.setObjectName("username_btn")
                MainWindow.setCentralWidget(self.centralwidget)

                MainWindow.setWindowTitle("Login Portal")
                self.submit_login.setText("Login")
                self.label_needacc.setText("Need an Account?")
                self.signup_btn.setText("Signup!")
                
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.submit_login.clicked.connect(self.login)
                self.signup_btn.clicked.connect(self.signup)
        
        def signup(self):
                self.hide()
                self.window = QtWidgets.QMainWindow()
                self.ui = Signup()
                self.ui.setupUi(self.window)
                self.window.show()

                
        def login(self):
                while True:
                        username = self.edit_username.text()
                        password = self.edit_password.text()
                        try:
                                con = sql.connect('users.db')
                                cursor = con.cursor()
                                find_user = ("SELECT * FROM users WHERE username = ? AND password = ?")
                                cursor.execute(find_user, [(username), (password)])
                                result = cursor.fetchall()
                                if result:
                                        for i in result:
                                                name = i[3]
                                        self.label_error.setText(f"Welcome {name}")
                                        QApplication.processEvents()
                                        self.hide()
                                        self.window = QtWidgets.QMainWindow()
                                        self.ui = main()
                                        self.ui.setupUi(self.window)
                                        self.window.show()

                                else:
                                        self.label_error.setText("Username/Password is incorrect")
                                        self.edit_password.clear()
                                        self.edit_username.clear()
                                        QApplication.processEvents()
                                break
                        except sql.Error as e:
                                print("Error while connecting ", e)
                                break


                        

if __name__ == "__main__":
        app = QApplication(sys.argv)
        w = Login()
        w.show()
        sys.exit(app.exec_())