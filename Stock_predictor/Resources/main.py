from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from pandas_datareader import data
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import csv
from datetime import datetime
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
import os
import time

class main(QtWidgets.QWidget):
        def __init__(self):
                QtWidgets.QWidget.__init__(self)
                self.setupUi(self)
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
                "      position: relative;\n"
                "      padding: 0;\n"
                "      border-width: 0;\n"
                "      outline: none;\n"
                "      border-radius: 2px;\n"
                "      background-color: #c4001d;\n"
                "      color: #ecf0f1;\n"
                "      border-radius: 5px;\n"
                "}")
                self.process.setObjectName("process")
                QtCore.QMetaObject.connectSlotsByName(Form)

                self.Result = QtWidgets.QLabel(self.frame_5)
                self.Result.setGeometry(QtCore.QRect(220, 20, 780, 70))
                self.Result.setText("")
                self.Result.setObjectName("Result")
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(11)
                self.Result.setFont(font)

                Form.setWindowTitle("User Stock Portal")
                self.label_sname.setText("Enter Stock Name")
                self.label_sday.setText("Enter Day")
                self.process.setText("Process")

                self.process.clicked.connect(self.Process)

        def Process(self):
                self.Result.setText("Please wait while the Models are being Trained....")
                time.sleep(3)
                START_DATE = '2020-01-01'
                END_DATE = str(datetime.now().strftime('%Y-%m-%d'))

                user_input = self.edit_sname.text()
                user_input = str(user_input).upper()
                try:
                        symbols = get_nasdaq_symbols()
                        stocks = data.DataReader(user_input, 'yahoo', START_DATE, END_DATE)
                except RemoteDataError:
                        self.label_error.setText("No data found, Try Again")
                        QApplication.processEvents()

                stock_data = pd.DataFrame(stocks)
                sym_data = pd.DataFrame(symbols[['Security Name']])

                if os.path.isfile('data.csv'):
                        print('File already exists')
                        os.remove('data.csv')
                        file = pd.DataFrame(stock_data)
                        file.to_csv('data.csv')
                else:
                        file = pd.DataFrame(stock_data)
                        file.to_csv('data.csv')

                symbols_data = sym_data.index.tolist()

                if user_input in symbols_data:
                        self.label_error.setText(f"{(sym_data.loc[user_input])}")
                        QApplication.processEvents()
                else:
                        self.label_error.setText("Stock Name not found!")
                        self.close()
                        QApplication.processEvents()

                df_read = pd.read_csv('data.csv')
                dates = []
                prices = []

                #Get the all data except for the last row
                df = df_read.head(len(df_read)-1)

                df_dates = df.loc[:,'Date']
                df_open = df.loc[:,'Open']

                #create independant data set X as dates
                for date in df_dates:
                        dates.append([int(date.split('-')[2])])

                #create the independant y data set as prices
                for open_price in df_open:
                        prices.append(float(open_price))    
                
                
                self.Result.clear()
                self.Result.setText("Make sure to save the chart window or close it for the final results")
                QApplication.processEvents()
                
                def predict_prices(dates, prices, x):
                        #create 3 svr models
                        svr_lin = SVR(kernel='linear', C=1e3)
                        svr_poly = SVR(kernel='poly', C=1e3, degree=2)
                        svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

                        #train the models on the dates and prices
                        svr_lin.fit(dates, prices)
                        svr_poly.fit(dates, prices)
                        svr_rbf.fit(dates, prices)

                        #Linear Regeression Model
                        lin_reg =  LinearRegression()
                        #Train the model
                        lin_reg.fit(dates, prices)

                        #plot the models on a graph to see which is best
                        plt.scatter(dates, prices, color='black', label='Data')
                        plt.scatter(dates, svr_rbf.predict(dates), color='red', label='RBF')
                        plt.scatter(dates, svr_lin.predict(dates), color='green', label='Linear')
                        plt.scatter(dates, svr_poly.predict(dates), color='blue', label='Polynomial')
                        plt.scatter(dates, lin_reg.predict(dates), color='orange', label='Linear Reg')
                        plt.xlabel('Days')
                        plt.ylabel('Price')
                        plt.title("Support Vector Regression")
                        plt.legend()
                        plt.show()

                        #return all three models
                        return(f"RBF: {round(svr_rbf.predict(x)[0], 2)} \t\t Linear: {round(svr_lin.predict(x)[0], 2)} \nPolynomial: {round(svr_poly.predict(x)[0], 2)} \t Linear Regression {round(lin_reg.predict(x)[0], 2)}")

                d = float(self.edit_sday.text())
                predicted = predict_prices(dates, prices, [[d]])
                self.Result.clear()
                self.Result.setText(f"{predicted}")
                QApplication.processEvents()
                
