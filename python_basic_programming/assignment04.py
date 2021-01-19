# -*- coding: utf-8 -*-
""" 
학번 : 20161048, 이름 : 이유리
과제번호 : 과제 4
제출일 : 2016.10.02
"""

import turtle #모든 turtle 함수 호출
turtle.setup(500,500) #화면 크기를 500x500으로 설정

def drawCircle(turt, x, y, radius, b_color, f_color, poly): #원을 그리는 함수 정의
    turt.color(b_color)
    turt.fillcolor(f_color)
    turt.penup()
    turt.goto(x,y-radius)
    turt.begin_fill()
    turt.pendown()
    turt.circle(radius, steps=poly)
    turt.end_fill()
    
def main(): #drawCircle 함수를 이용하여 원을 그리는 것을 실제로 시행하기 위한 함수 정의
    
    tut_window=turtle.Screen()
    tut_window.bgcolor('black') #배경화면의 색상 설정
    
    myturt=turtle.Turtle() #turtle 함수를 사용하기 위해 변수에 저장
    
    circle_X=-125
    circle_R= 125
    
    for n in range(6): #6개의 원을 반복적으로 그리기 위한 반복문
        if (n%2 == 0):
            drawCircle(myturt, circle_X , 0 , circle_R , 'magenta', 'magenta', None)
        else:
            drawCircle(myturt, circle_X , 0 , circle_R , 'cyan', 'cyan', None)
            
        circle_R=circle_R//2
        circle_X=circle_X+3*circle_R
        
    myturt.hideturtle() #도형을 다 그린 후에 turtle 아이콘을 보이지 않게 함
    turtle.done()

main()