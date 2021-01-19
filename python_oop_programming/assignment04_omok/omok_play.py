#-*- coing:utf-8 -*-

from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPixmap

class Omok_stone(QGraphicsItem):

    def __init__(self):

        super().__init__()


        self.board = [[-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1],
                      [-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1,-1,-1, -1, -1,-1]]
        self.turn = 0


    
    def reset(self):

        for x in range(19):
            for y in range(19):
                self.board[x][y] = -1

        self.turn = 0
        self.update()


    def select(self, x, y): 
        if x < 0 or y < 0 or x >=19 or y >=19:
            return
        if self.board[x][y] == -1:
            self.board[x][y] = self.turn #0이 검정, 1이 하양

            self.turn = 1  - self.turn
            
            
    def boundingRect(self):

        return QRectF(0,0,760,760)
    
    def paint(self, painter, option, widget):               

        for x in range(19):
            for y in range(19):
                if self.board[x][y] == 0:        
                    
                    black = QPixmap('black.png')
                    
                    painter.drawPixmap(40*x+1, 40*y+1, black)
                    
                elif self.board[x][y] == 1:
                    
                    white = QPixmap('white.png')

                    painter.drawPixmap(40*x+1, 40*y+1, white)
    
    def mousePressEvent(self, event):

        pos = event.pos()

        self.select(int(pos.x()/40), int(pos.y()/40))
        self.update()

        super().mousePressEvent(event)
            