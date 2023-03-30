import sys
import os
from business import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_3.clicked.connect(self.finan)
     self.ui.pushButton.clicked.connect(self.trans)
     self.ui.pushButton_2.clicked.connect(self.crcsv)
     self.ui.pushButton_5.clicked.connect(self.gnb)
     self.ui.pushButton_6.clicked.connect(self.qda)
     self.ui.pushButton_7.clicked.connect(self.knn)
     self.ui.pushButton_8.clicked.connect(self.bc)

  def finan(self):
    os.system("python finan1.py")
	
  def trans(self):
    os.system("python trans1.py")

  def crcsv(self):
    os.system("python createcsv1.py")
	
  def gnb(self):
    os.system("python -W ignore gnb1.py")

  def qda(self):
    os.system("python -W ignore qda1.py")
	
  def knn(self):
    os.system("python -W ignore knn1.py")

  def bc(self):
    os.system("python -W ignore bc1.py")
   
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
