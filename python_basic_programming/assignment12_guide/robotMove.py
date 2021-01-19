#-*- coding:utf-8 -*-

import turtle
import time

# 윈도우 스크린의 크기를 지정하기 위해 Screen 객체 생성
screen = turtle.Screen()     

# 왼쪽, 오른쪽, 위, 아래를 향하는 로봇의 이미지 지정  (turtle의 이미지는 gif 유형만 허용됨
image = {"left":"robot_Leftward.gif", "up":"robot_Upward.gif", "right":"robot_Rightward.gif",  
         "down":"robot_Downward.gif", "gem":"gem.gif"}

def addImages():
    # image 딕셔너리에 지정된 로봇에 대한 이미지를  Screen 객체에 추가 
    for direction in image:
        screen.addshape(image[direction])
        
    screen.addshape(image["gem"])
        
def drawRobot(myRobot, direction, robotPos):
    # 로봇의 이동방향에 따라  로봇 이미지를 지정한 후, 이동할 위치에 로봇 이미지를 그려줌 '''
    step = 100              # 로봇의 한번 이동시의 픽셀의 크기
    myRobot.clear()         # 화면에 보여줌 직전 이미지를 지움
    myRobot.showturtle()
    # 이동 방향에 따른 로솝 이미지를 지정하고 로봇의 위치 좌표를 변경
    if direction == "up":                
        myRobot.shape(image["up"])
        robotPos[1] += 1  
    elif direction == "down":
        myRobot.shape(image["down"])
        robotPos[1] -= 1
    elif direction == "left":
        myRobot.shape(image["left"])
        robotPos[0] -= 1
    elif direction == "right":
        myRobot.shape(image["right"])
        robotPos[0] += 1
        
    myRobot.penup()         # 로봇을 이동시 궤적을 나타내지 않도록 하기 위해 penup()을 실행
    myRobot.goto(robotPos[0]*step, robotPos[1]*step)      # 지정된 위치로 로봇을 이동
  
def main(): 
    screen.setup(700, 700)              # 화면의 크기를 지정 ,  turtle.setup(700, 700) 대신 사용
    addImages()                         # 로봇, 보석 이미지를 사용하기 위해 이미지 추가하는 함수를 호출

    gemPen = turtle.Turtle()            # 보석을 보여주기 위한 turtle 객체를 생성
    gemPen.shape(image["gem"])
    gemPen.hideturtle()
    gemPen.penup()
    gemPen.goto(-300, 300)
    gemPen.showturtle()

    robot = turtle.Turtle()             # robot의 움직임을 보여주기 위한 turtle 객체 생성ㄹ
    robot.hideturtle()
     
    robotPos = [0, 0]                   # 로솝의 최초 위치 지정

    for direction in image:             # 네 방향으로의 움직임을 보여 주기 위해 image 딕셔너리의 아이템 모두를 선택하여 반복
        drawRobot(robot, direction, robotPos)   # 로봇을 화면에 그림
        time.sleep(1)                           # 로솝을 잠시 멈추도록 하기 위해 ...
      
    turtle.done()
    
main()