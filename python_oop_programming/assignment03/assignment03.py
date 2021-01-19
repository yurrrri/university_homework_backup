import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()       
        
        uic.loadUi('Calculator.ui', self)

        self.operator = None
        self.before = None
        self.after = None
        self.count = 0
        
        self.show()
        
    @pyqtSlot()
    def show_number(self):
        val = self.num_Edt.text()
        if self.sender() == self.dot_btn : 
            if '.' not in val : 
                self.num_Edt.setText(self.num_Edt.text() + self.sender().text())
        else :  
            if val == '0'  or self.check == True: 
                self.num_Edt.setText(self.sender().text()) 
                self.check = False
            else :          
                self.num_Edt.setText(self.num_Edt.text()+self.sender().text())
                                 
    @pyqtSlot()
    def operator(self):
        
        if self.before == None:
            self.before = self.num_Edt.text()
            self.operator = self.sender().text()
        else:
            self.after = self.num_Edt.text()
            
        if self.before !=None and self.after !=None and self.operator !=None:
            answer = eval(self.before + self.operator + self.after)
            self.before = str(answer)
            self.operator = self.sender().text()
            self.num_Edt.setText(self.before) 
            
        self.check = True
                
    @pyqtSlot()
    def change(self):
        
        cur_num = eval(self.num_Edt.text())
        
        if self.sender() == self._pm_btn :
            
            cur_num = cur_num * (-1)
            
            self.num_Edt.setText(str(cur_num))
            
        elif self.sender() == self.fraction_btn :
            
            cur_num = 1/cur_num
            
            self.num_Edt.setText(str(cur_num))
        
        elif self.sender() == self.sqrt_btn:
            
            cur_num = math.sqrt(cur_num)
            
            self.num_Edt.setText(str(cur_num))
            
        elif self.sender() == self.sqr_btn:
            
            cur_num = cur_num ** 2
            
            self.num_Edt.setText(str(cur_num))
        
        self.check = True
        
        
    @pyqtSlot()
    def result(self):
        
        self.after = self.num_Edt.text()
        
        cal = eval(self.before + self.operator + self.after)
        self.num_Edt.setText(str(cal))
            
        self.before = None
        self.after = None
        self.operator = None
        
        self.check = True
               
    @pyqtSlot()
    def clear(self):

        self.num_Edt.setText('0')
        
        self.before = None
        self.operator = None
        self.after = None
        
    @pyqtSlot()
    def clear_one(self):
        
        self.num_Edt.setText('0')
        
        self.after = None
           
    @pyqtSlot()
    def erase(self):
        self.num_Edt.backspace()
 
 
def main():
    app = QApplication(sys.argv)
    l = Calculator()
    sys.exit(app.exec())

main()