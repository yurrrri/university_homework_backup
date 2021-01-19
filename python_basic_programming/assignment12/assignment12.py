#-*- coding:utf-8 -*-

'''
학번: 20161048 이름: 이유리
과제번호: 과제 12 (미로찾기 2)
제출일자: 2016.11.15
'''
from yuri import lectureTurtle as LT
import turtle
import time
from random import randint

screen = turtle.Screen()
size=50
image = {"left":"robot_Leftward.gif", "up":"robot_Upward.gif", "right":"robot_Rightward.gif",  
         "down":"robot_Downward.gif", "gem":"gem.gif"}
            

def firstblocklist():
    
    firstblock=[]
    
    openfirst=open('stage1.txt','r')
    
    for line in openfirst:
        x,y=line.split(',')
        x=int(x); y=int(y)
        firstblock.append([x,y])
        
    openfirst.close()
    
    return firstblock

def firstGrid():
    
    first=firstblocklist()
    
    mazePen=turtle.Turtle()
    mazePen.hideturtle()
    mazePen.speed(0)
    
    stagepen=turtle.Turtle()
    stagepen.hideturtle()
    
    for posX in range(-5,6):
        for posY in range(-5,6):
            currentPos = [posX,posY]
            if currentPos in first:
                LT.drawRectangle(mazePen, 50*posX, 50*posY, size, size, 'white', 'black')
            else:
                LT.drawRectangle(mazePen, 50*posX, 50*posY, size, size, 'black', 'white')
        
        LT.writeText(mazePen, posX, -300, posX*size)
        LT.writeText(mazePen, posX, size*posX, 290)
        
    stagepen.penup()
    stagepen.goto(-275,350)
    stagepen.pendown()
    stagepen.pencolor('green')
    stagepen.write('stage1',font=('impact',17,'italic'))

def secondblocklist():
    
    secondblock=[]
    
    opensecond=open('stage2.txt','r')
    
    for line in opensecond:
        x,y=line.split(',')
        x=int(x); y=int(y)
        secondblock.append([x,y])
        
    opensecond.close()
    
    return secondblock
        
def secondGrid():
    
    second=secondblocklist()
    
    mazePen=turtle.Turtle()
    mazePen.hideturtle()
    mazePen.speed(0)
    
    stagepen=turtle.Turtle()
    stagepen.hideturtle()

    for posX in range(-5,6):
        for posY in range(-5,6):
            currentPos = [posX,posY]
            if currentPos in second:
                LT.drawRectangle(mazePen, 50*posX, 50*posY, size, size, 'white', 'black')
            else:
                LT.drawRectangle(mazePen, 50*posX, 50*posY, size, size, 'black', 'white')
        
        LT.writeText(mazePen, posX, -300, posX*size)
        LT.writeText(mazePen, posX, size*posX, 290)
    
    stagepen.penup()
    stagepen.goto(-275,350)
    stagepen.pendown()
    stagepen.pencolor('blue')
    stagepen.write('stage2',font=('impact',17,'italic'))
    
def addImages():
    
    for direction in image:
        screen.addshape(image[direction])
    
def makeGem():
    
    addImages()
    
    gemPen = turtle.Turtle()
    gemPen.shape(image["gem"])
    gemPen.hideturtle()
    gemPen.penup()
    gemPen.goto(-250,250)
    gemPen.showturtle()
        
def firstnextRobot(pen,currentPos):
    first=firstblocklist()
    
    pen.clear()
    pen.showturtle()

    repeatFlag=True
    
    while repeatFlag:
        nextPos=currentPos[:]
        
        a=randint(1,4)
        
        if a==1:
            pen.shape(image["right"])
            nextPos[0]+=1
        elif a==2:
            pen.shape(image["left"])
            nextPos[0]-=1
        elif a==3:
            pen.shape(image["up"])
            nextPos[1]+=1
        else:
            pen.shape(image["down"])
            nextPos[1]-=1
            
        pen.penup()
        
        if nextPos not in first and -5<=nextPos[0]<=5 and -5<=nextPos[1]<=5:
            repeatFlag=False
            
    pen.goto(nextPos[0]*size, nextPos[1]*size)  
         
    return nextPos

def secondnextRobot(pen,currentPos):
    second=secondblocklist()
    
    pen.clear()
    pen.showturtle()

    repeatFlag=True
    
    while repeatFlag:
        nextPos=currentPos[:]
        
        a=randint(1,4)
        
        if a==1:
            pen.shape(image["right"])
            nextPos[0]+=1
        elif a==2:
            pen.shape(image["left"])
            nextPos[0]-=1
        elif a==3:
            pen.shape(image["up"])
            nextPos[1]+=1
        else:
            pen.shape(image["down"])
            nextPos[1]-=1
            
        pen.penup()
        
        if nextPos not in second and -5<=nextPos[0]<=5 and -5<=nextPos[1]<=5:
            repeatFlag=False
            
    pen.goto(nextPos[0]*size, nextPos[1]*size)   
         
    return nextPos
        
def stageone():
    textPen=turtle.Turtle()
    textPen.hideturtle()
    
    robotPen=turtle.Turtle()
    robotPen.hideturtle()
    robotPen.speed(0)
    
    robotPos=[5,-5]
    gemPos=[-5,5]
    count=0

    makeGem()
    
    robotPen.penup()
    robotPen.shape(image['up'])
    robotPen.goto(robotPos[0]*size, robotPos[1]*size)
    time.sleep(.5)
    
    while robotPos !=gemPos:
        time.sleep(.5)
        robotPos=firstnextRobot(robotPen,robotPos)
        count+=1
        
    textPen.penup()
    textPen.goto(-275,320)
    textPen.pendown()
    textPen.pencolor('black')
    textPen.write('축하합니다. %d번만에 보물창고에 도착하셨습니다.' %count,font=('normal',13,'italic'))
    time.sleep(1)
    
def stagetwo():
    textPen=turtle.Turtle()
    textPen.hideturtle()
    
    robotPen=turtle.Turtle()
    robotPen.hideturtle()
    robotPen.speed(0)
    
    robotPos=[5,-5]
    gemPos=[-5,5]
    count=0

    makeGem()
    
    robotPen.penup()
    robotPen.shape(image['up'])
    robotPen.goto(robotPos[0]*size, robotPos[1]*size)    
    time.sleep(.5)
    
    while robotPos !=gemPos:
        time.sleep(.5)
        robotPos=secondnextRobot(robotPen,robotPos)
        count+=1
        
    textPen.penup()
    textPen.goto(-275,320)
    textPen.pendown()
    textPen.pencolor('black')
    textPen.write('축하합니다. %d번만에 보물창고에 도착하셨습니다.' %count,font=('normal',13,'italic'))
    time.sleep(1)

def main():
    firstGrid()
    stageone()
    
    screen.clear()
    
    secondGrid()
    stagetwo()
        
main()