# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finan.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 213)
        MainWindow.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 150, 331, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 20, 111, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 251, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 50, 111, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(410, 80, 111, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(410, 110, 111, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 251, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 261, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 251, 21))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Statistics"))
        self.pushButton.setText(_translate("MainWindow", "Store Financial Statistics in Data base"))
        self.lineEdit_4.setText(_translate("MainWindow", "5000000"))
        self.label_4.setText(_translate("MainWindow", "Current Balance(0 to 100000000)"))
        self.lineEdit_5.setText(_translate("MainWindow", "500000000"))
        self.lineEdit_6.setText(_translate("MainWindow", "500000000"))
        self.lineEdit_7.setText(_translate("MainWindow", "100"))
        self.label_6.setText(_translate("MainWindow", "Year Inflow(0 to 100000000000)"))
        self.label_7.setText(_translate("MainWindow", "Year Outflow(0 to 100000000000)"))
        self.label_8.setText(_translate("MainWindow", "No.ofchequeBounces(0 to 10000)"))


