# -*- coding:utf-8 -*-

import turtle
import time
from random import randint as randi
from mazeAssignment import lectureTurtle as tut

screen = turtle.Screen()
image = {"left":"robot_Leftward.gif", "right":"robot_Rightward.gif", "up":"robot_Upward.gif", 
         "down":"robot_Downward.gif", "gem":"gem.gif"}

blockList = []
gemPos = [-5, 5]
side = 50

def getStageData(stageNo):
    blockList.clear()
    inputFile = open('stage'+str(stageNo) + '.txt', 'r')
    for point in inputFile:
        x, y = point.split(',')
        x, y = int(x), int(y)
        blockList.append([x, y])
    
def addImagesToScreen():
    for direction in image:
        screen.addshape(image[direction])
    screen.addshape(image['gem'])

def drawGem():
    gemPen = turtle.Turtle()
    gemPen.shape(image['gem'])
    gemPen.hideturtle()
    gemPen.penup()    
    gemPen.goto(gemPos[0]*side, gemPos[1]*side)
    gemPen.showturtle()
    
def drawMaze():
    mazePen = turtle.Turtle()
    mazePen.hideturtle()
    mazePen.speed(0)
    
    tut.drawRectangle(mazePen, 0, 0, side*11, side*11, b_color='black')
    for x in range(-5, 6):
        tut.writeText(mazePen, x, x*side, 5.7*side, t_color='black')
        tut.writeText(mazePen, x, -5.8*side, x*side, t_color='black')                 
        for y in range(-5, 6):
            cell = [x, y]
            if cell in blockList:        
                tut.drawRectangle(mazePen, cell[0]*side, cell[1]*side, side, side, b_color='black', f_color='black')
            else:
                tut.drawRectangle(mazePen, cell[0]*side, cell[1]*side, side, side, b_color='black', f_color='white')
    tut.writeText(mazePen, '횟수 : ', -250, 330, font=2)
    drawGem()
    #tut.drawRectangle(pen, gemPos[0]*side, gemPos[1]*side, side, side, b_color='black', f_color='red')
        
    
    
def getNextPosition(robotPen, robotPos) :    
    repeatFlag = True
    
    while repeatFlag:
        nextRobotPos = list(robotPos)
        
        dirVal = randi(1, 4)        
        if dirVal == 1 :            
            nextRobotPos[0] -= 1
            direction ="left"            
        elif dirVal == 2 :
            nextRobotPos[0] += 1
            direction = "right"    
        elif dirVal == 3 :
            nextRobotPos[1] -= 1
            direction = "down"    
        else :
            nextRobotPos[1] += 1
            direction = "up"    
    
        if nextRobotPos not in blockList and -5<=nextRobotPos[0]<=5 and -5<=nextRobotPos[1]<=5 : 
            repeatFlag = False
    
    robotPen.shape(image[direction])        
    return nextRobotPos    

def moveRobot(robot, robotPos):
    robot.clear()    
    robot.speed(0)
    robot.penup()
    robot.goto(robotPos[0]*side, robotPos[1]*side)

def writeMoveNum(pen, num):
    pen.clear()     
    tut.writeText(pen, str(num), -200, 330, font=2)      
    
def findGem():
    textPen = turtle.Turtle()    # 이동 횟수를 출력하기 위한 turtle 객체
    textPen.hideturtle()
    textPen.shape()
    
    robotPen = turtle.Turtle()   # 로봇을 그리기 위한 turtle 객체    
    robotPen.showturtle()  
    robotPen.shape(image["left"])
    noMove = 0  
    initialRobotPos = [5, -5]
    
            
    moveRobot(robotPen, initialRobotPos)    
    writeMoveNum(textPen, noMove)    
    time.sleep(2)
    
    currentRobotPos = list(initialRobotPos)
    while currentRobotPos != gemPos:            
        currentRobotPos = getNextPosition(robotPen, currentRobotPos)        
        noMove += 1
        moveRobot(robotPen, currentRobotPos)
        writeMoveNum(textPen, noMove)
        time.sleep(0.5)                      
        
def main():
    screen.setup(750, 750)
    noStages = 2
    addImagesToScreen()
    
    for stage in range(1, noStages+1):
        screen.clear()
        getStageData(stage) 
        
        drawMaze()
        findGem()
        
    turtle.done()    
main()    
