#-*- coing:utf-8 -*-

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtCore import Qt, QLineF, QRectF, pyqtSlot
from PyQt5.QtGui import QPen, QBrush, QColor, QPixmap

from omok_play import Omok_stone

class Omok(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('omok.ui', self)
        self.initUi()
        
        self.show()
        
    def initUi(self):
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 760, 760)
        self.omok.setScene(self.scene)
        
        pixmap = QPixmap('background_wood.png')
        self.scene.addPixmap(pixmap)

        self.draw_rect()
        self.draw_line()
        self.draw_circle()
        
        self.omok_stone = Omok_stone()
        self.scene.addItem(self.omok_stone)

            
    def draw_line(self):
        pen = QPen(Qt.black, 2)
        cross_pen = QPen(Qt.black, 3)
        
        for i in range(19):
            self.scene.addLine(QLineF(40*i+60, 20, 40*i+60, 740), pen)
            self.scene.addLine(QLineF(20, 40*i+60, 740, 40*i+60), pen)
            
        for i in range(3):
            self.scene.addLine(QLineF(20+40*(6*i+3), 20, 20+40*(6*i+3), 740), cross_pen)
            self.scene.addLine(QLineF(20, 20+40*(6*i+3), 740, 20+40*(6*i+3)), cross_pen)
        

    def draw_rect(self):
        pen = QPen(Qt.black, 3)
        
        rect = QRectF(20, 20, 720, 720)
        self.scene.addRect(rect, pen)

    def draw_circle(self):
        pen = QPen(Qt.black, 4)
        brush = QBrush(QColor(0, 0, 0))
        
        for i in range(3):
            self.scene.addEllipse(QRectF(136+240*i, 136, 8,8), pen,brush)
            self.scene.addEllipse(QRectF(136+240*i, 376, 8,8), pen,brush)
            self.scene.addEllipse(QRectF(136+240*i, 616, 8,8), pen,brush)
            
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        
        for x in range(15):
            for y in range(19):
                if self.omok_stone.board[x][y]==0 and self.omok_stone.board[x+1][y]==0 and self.omok_stone.board[x+2][y]==0 and self.omok_stone.board[x+3][y]==0 and self.omok_stone.board[x+4][y]==0:
                    self.p1_score.setText('Win')
                    self.p2_score.setText('Lose')
                    
        for x in range(19):
            for y in range(15):
                if self.omok_stone.board[x][y]==0 and self.omok_stone.board[x][y+1]==0 and self.omok_stone.board[x][y+2]==0 and self.omok_stone.board[x][y+3]==0 and self.omok_stone.board[x][y+4]==0:
                    self.p1_score.setText('Win')
                    self.p2_score.setText('Lose') 
                    
        for x in range(15):
            for y in range(19):
                if self.omok_stone.board[x][y]==1 and self.omok_stone.board[x+1][y]==1 and self.omok_stone.board[x+2][y]==1 and self.omok_stone.board[x+3][y]==1 and self.omok_stone.board[x+4][y]==1:
                    self.p1_score.setText('Lose')
                    self.p2_score.setText('Win')
                    
        for x in range(19):
            for y in range(15):
                if self.omok_stone.board[x][y]==1 and self.omok_stone.board[x][y+1]==1 and self.omok_stone.board[x][y+2]==1 and self.omok_stone.board[x][y+3]==1 and self.omok_stone.board[x][y+4]==1:
                    self.p1_score.setText('Lose')
                    self.p2_score.setText('Win')
                    
        for x in range(15):
            for y in range(15):
                if self.omok_stone.board[x][y]==0 and self.omok_stone.board[x+1][y+1]==0 and self.omok_stone.board[x+2][y+2]==0 and self.omok_stone.board[x+3][y+3]==0 and self.omok_stone.board[x+4][y+4]==0:
                    self.p1_score.setText('Win')
                    self.p2_score.setText('Lose')
                    
        for x in range(15):
            for y in range(15):
                if self.omok_stone.board[x][y]==1 and self.omok_stone.board[x+1][y+1]==1 and self.omok_stone.board[x+2][y+2]==1 and self.omok_stone.board[x+3][y+3]==1 and self.omok_stone.board[x+4][y+4]==1:
                    self.p1_score.setText('Lose')
                    self.p2_score.setText('Win')
                    
    @pyqtSlot()
    def reset(self):
        self.omok_stone.reset()
        self.p1_score.setText('')
        self.p2_score.setText('')
    
    
def main():
    app = QApplication(sys.argv)
    omok = Omok()
    
    sys.exit(app.exec())

main()