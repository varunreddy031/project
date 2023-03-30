import sys
from finan import *
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
        cb = str(self.ui.lineEdit_4.text())
        yi = str(self.ui.lineEdit_5.text())
        yo = str(self.ui.lineEdit_6.text())
        ncb = str(self.ui.lineEdit_7.text())
        cur.execute('INSERT INTO finan VALUES(?,?,?,?)',(cb,yi,yo,ncb))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


