import sys
from trans import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
con = sqlite3.connect('business1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues) 

   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        mt = str(self.ui.lineEdit_4.text())
        ot = str(self.ui.lineEdit_5.text())
        tt = str(self.ui.lineEdit_6.text())
        ft = str(self.ui.lineEdit_7.text())
        ca = str(self.ui.lineEdit_9.text())
        oa = str(self.ui.lineEdit_8.text())		
        cur.execute('INSERT INTO trans VALUES(?,?,?,?,?,?)',(mt,ot,tt,ft,ca,oa))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


