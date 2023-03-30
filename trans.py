# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trans.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 292)
        MainWindow.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 220, 301, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 20, 111, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 261, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(320, 50, 111, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(320, 80, 111, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(320, 110, 111, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 281, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 301, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 301, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(320, 170, 111, 33))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 140, 251, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 170, 271, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(320, 140, 111, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transactional Statistics"))
        self.pushButton.setText(_translate("MainWindow", "Store Transactional Statistics in Data base"))
        self.lineEdit_4.setText(_translate("MainWindow", "50000"))
        self.label_4.setText(_translate("MainWindow", "Manual Transactions(0 to 1000000 )"))
        self.lineEdit_5.setText(_translate("MainWindow", "500000"))
        self.lineEdit_6.setText(_translate("MainWindow", "550000"))
        self.lineEdit_7.setText(_translate("MainWindow", "50000"))
        self.label_6.setText(_translate("MainWindow", "Online Transactions(0 to1000000000 )"))
        self.label_7.setText(_translate("MainWindow", "Total Transactions(0 to 100000000000 )"))
        self.label_8.setText(_translate("MainWindow", "No.of Failed Transactions(0 to 10000000)"))
        self.lineEdit_8.setText(_translate("MainWindow", "5000"))
        self.label_9.setText(_translate("MainWindow", "No.Of Closed Accounts(0 to 1000 )"))
        self.label_10.setText(_translate("MainWindow", "New Accounts Opened(0 to 10000 )"))
        self.lineEdit_9.setText(_translate("MainWindow", "500"))


