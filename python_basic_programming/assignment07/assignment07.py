#-*- coding : utf-8 -*-
"""
학번:20161048 이름:이유리
과제번호 : 과제7
제출일자 : 2016.10.11
"""


import turtle
from yuri import lectureTurtle
from random import randint as randi

def main():
    turtle.setup(650,650)
    
    myTurtle=turtle.Turtle()
    myTurtle.speed(5)
    
    n=11
    size=50
    
    x=-250
    y=250
    
    for num in range(n):
        for k in range(n):
            lectureTurtle.drawRectangle(myTurtle, x , y , size ,size, b_color='black', f_color=None)
            x=x+size
            
        x=-250
        y=y-size
    
    myTurtle.penup()
    myTurtle.goto(0,0)
    myTurtle.pensize(3)
    myTurtle.color('red')
    myTurtle.pendown()
    myTurtle.shape('turtle')
    myTurtle.showturtle()
    
    x=0 #거북이가 시작할 때의 x좌표
    y=0 #거북이가 시작할 때의 y좌표
    count=0 #플레이보드에서 거북이가 움직인 횟수를 세기 위한 변수
    
    while abs(x)<=275 and abs(y)<=275:
        r=randi(1,4)
        if r==1:
            x=x+size
        elif r==2:
            x=x-size
        elif r==3:
            y=y+size
        elif r==4:
            y=y-size
        myTurtle.goto(x,y)
        
        count+=1
        
    lectureTurtle.writeText(myTurtle, '%d번의 움직임 만에 플레이 보드를 벗어났습니다' %count, -275, 300)
    
    myTurtle.hideturtle()
    turtle.done()
main()