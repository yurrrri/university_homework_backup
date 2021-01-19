# -*- coding: utf-8 -*-
""" 
학번 : 20161048, 이름 : 이유리
과제번호 : 과제 5
제출일 : 2016.10.03
"""

import turtle #모든 turtle 함수 호출
import lectureTurtle #모든 lectureTurtle 함수 호출

def main(): #lectureTurtle 함수를 이용하여 도형을 그리기 위한 함수 정의
    turtle.setup(500, 500) #스크린의 크기를 500x500으로 설정
    my_Turtle = turtle.Turtle() #turtle 함수를 사용하기 위해 변수에 저장
    my_Turtle.hideturtle() #도형을 그린 후 turtle 아이콘을 화면에서 보이지 않게 함
    
    lectureTurtle.writeText(my_Turtle, '생일을 축하합니다! ', -40, 225)
    lectureTurtle.drawRectangle(my_Turtle, 0, -37.5,  200, 75, f_color='indianred')
    lectureTurtle.drawRectangle(my_Turtle, 0, 25, 150, 50, f_color='cornflowerblue')
    lectureTurtle.drawRectangle(my_Turtle, 0, 75, 100, 50, f_color='cornflowerblue')
    lectureTurtle.drawRectangle(my_Turtle, 0, 112.5, 50, 25, f_color='darkkhaki')
    lectureTurtle.drawRectangle(my_Turtle, 0, 137.5, 25, 25, f_color='darkkhaki')
    lectureTurtle.drawPolygon(my_Turtle, -56.25, -10, 20 , 3, f_color='forestgreen')
    lectureTurtle.drawPolygon(my_Turtle, -18.75, -10, 20 , 3, f_color='forestgreen')
    lectureTurtle.drawPolygon(my_Turtle, 18.75, -10, 20 , 3, f_color='forestgreen')
    lectureTurtle.drawPolygon(my_Turtle, 56.25 , -10, 20 , 3, f_color='forestgreen')
    lectureTurtle.drawCircle(my_Turtle, -87.5, 12.5, 12.5, f_color='red')
    lectureTurtle.drawCircle(my_Turtle, 87.5, 12.5, 12.5, f_color='red')
    lectureTurtle.drawCircle(my_Turtle, 0, 162.5,  12.5, f_color='red')
    
    
    turtle.done()

main()