#-*- coding:utf-8 -*-

'''
학번: 20161048 이름: 이유리
과제번호: 과제 10
제출일자: 2016.10.30
'''

import turtle
from yuri import lectureTurtle as LT
import time
from random import randint

blocklst=[[-3,5],[-2,5],[-5,4],[-1,4],[0,4],[2,4],[3,4],[4,4],[-5,3],[-3,3],[-1,3],[2,3],[4,3],
[-5,2],[-4,2],[-3,2],[-1,2],[1,2],[2,2],[4,2],[-3,1],[-1,1],[1,1],[4,1],
[-4,0],[-3,0],[1,0],[3,0],[-4,-1],[-1,-1],[1,-1],[3,-1],[4,-1],[5,-1],[-4,-2],[-2,-2],[-1,-2],[3,-2],
[-2,-3],[1,-3],[5,-3],[-4,-4],[-3,-4],[-2,-4],[0,-4],[1,-4],[2,-4],[3,-4],[5,-4],[-4,-5],[3,-5]]

side=50

def drawGrid():
    
    gPen=turtle.Turtle()
    gPen.hideturtle()
    gPen.speed(0)

    for posX in range(-5,6):
        for posY in range(-5,6):
            currentPos = [posX,posY]
            if currentPos in blocklst:
                LT.drawRectangle(gPen, 50*posX, 50*posY, side, side, 'white', 'black')
            else:
                LT.drawRectangle(gPen, 50*posX, 50*posY, side, side, 'black', 'white')
        
        LT.writeText(gPen, posX, -300, posX*side)
        LT.writeText(gPen, posX, side*posX, 290)
    LT.drawRectangle(gPen, -250, 250, side, side, 'black', 'red' )
    
def drawRobot(pen, robotPos, robotR):
    pen.hideturtle()
    pen.clear()
    pen.speed(0)
    
    LT.drawCircle(pen, robotPos[0]*side, robotPos[1]*side, robotR , 'black','blue')
    
def nextPosition(currentPos):
    repeatFlag=True
    
    while repeatFlag:
        nextPos=currentPos[:]
        
        a=randint(0,1)
        b=randint(0,1)
        
        if b==0:
            nextPos[a]=nextPos[a]-1
        else:
            nextPos[a]=nextPos[a]+1
        
        if nextPos not in blocklst and -5<=nextPos[0]<=5 and -5<=nextPos[1]<=5:
            repeatFlag=False
        
    return nextPos
        
def start():
    sPen=turtle.Turtle()
    sPen.hideturtle()
    robotPos=[5,-5]
    boxPos=[-5,5]
    robotR=15
    count=0
    
    drawRobot(sPen, robotPos, robotR)
    
    while robotPos !=boxPos:
        time.sleep(0.5)
        robotPos=nextPosition(robotPos)
        count+=1
        drawRobot(sPen, robotPos, robotR)
    
    LT.writeText(sPen, '축하합니다. %s번만에 보물창고에 도착하셨습니다.' %count, -250 ,320)
    turtle.done()
    
def main():
    drawGrid()
    start()
    
main()