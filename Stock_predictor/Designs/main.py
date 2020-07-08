# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 797)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.frame.setStyleSheet("QFrame#frame\n"
"{\n"
"    background: #c4001d;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 20, 800, 150))
        self.frame_2.setStyleSheet("QFrame\n"
"{\n"
"    background: #ff1744;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_sname = QtWidgets.QLabel(self.frame_2)
        self.label_sname.setGeometry(QtCore.QRect(200, 30, 150, 30))
        self.label_sname.setStyleSheet("QLabel#label_sname\n"
"{\n"
"    color: white;\n"
"}")
        self.label_sname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sname.setObjectName("label_sname")
        self.edit_sname = QtWidgets.QLineEdit(self.frame_2)
        self.edit_sname.setGeometry(QtCore.QRect(350, 30, 300, 30))
        self.edit_sname.setObjectName("edit_sname")
        self.label_sday = QtWidgets.QLabel(self.frame_2)
        self.label_sday.setGeometry(QtCore.QRect(200, 80, 150, 30))
        self.label_sday.setStyleSheet("QLabel#label_sday\n"
"{\n"
"    color: white;\n"
"}")
        self.label_sday.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sday.setObjectName("label_sday")
        self.edit_sday = QtWidgets.QLineEdit(self.frame_2)
        self.edit_sday.setGeometry(QtCore.QRect(350, 80, 300, 30))
        self.edit_sday.setObjectName("edit_sday")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(0, 140, 800, 661))
        self.frame_3.setStyleSheet("QFrame#frame_3\n"
"{\n"
"    background: white;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.plotter = QtWidgets.QWidget(self.frame_3)
        self.plotter.setGeometry(QtCore.QRect(0, 60, 800, 501))
        self.plotter.setObjectName("plotter")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(0, 560, 800, 100))
        self.frame_5.setStyleSheet("QFrame\n"
"{\n"
"    background: #ffebee;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.Result = QtWidgets.QLabel(self.frame_5)
        self.Result.setGeometry(QtCore.QRect(220, 20, 421, 71))
        self.Result.setText("")
        self.Result.setObjectName("Result")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, -10, 800, 71))
        self.frame_4.setStyleSheet("QFrame\n"
"{\n"
"    background: #ff616f;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_error = QtWidgets.QLabel(self.frame_4)
        self.label_error.setEnabled(False)
        self.label_error.setGeometry(QtCore.QRect(200, 20, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("QLabel\n"
"{\n"
"    color: white;\n"
"}")
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.process = QtWidgets.QPushButton(self.frame_4)
        self.process.setGeometry(QtCore.QRect(500, 20, 150, 40))
        self.process.setStyleSheet("QPushButton\n"
"{\n"
"    position: relative;\n"
"    display: block;\n"
"      padding: 0;\n"
"      overflow: hidden;\n"
"    border-width: 0;\n"
"      outline: none;\n"
"      border-radius: 2px;\n"
"      box-shadow: 0 1px 4px rgba(0, 0, 0, .6);\n"
"      background-color: #c4001d;\n"
"      color: #ecf0f1;\n"
"      transition: background-color .3s;\n"
"    border-radius: 5px;\n"
"}")
        self.process.setObjectName("process")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_sname.setText(_translate("Form", "Enter Stock Name"))
        self.label_sday.setText(_translate("Form", "Enter Find Day"))
        self.process.setText(_translate("Form", "Process"))
