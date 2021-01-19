#-*- coding:utf-8 -*-

import turtle
import lectureTurtle

def main():
    turtle.setup(500, 500)
    myTut = turtle.Turtle()
    myTut.hideturtle()    
    
    lectureTurtle.writeText(myTut, 'lectureTurtle 함수 테스트 ', -50, 200)      
    lectureTurtle.drawLine(myTut, -250, 0, 250, 0)
    lectureTurtle.drawLine(myTut, 0, -250, 0, 250)
    lectureTurtle.drawPolygon(myTut, 0, 0,  50, 3, f_color='IndianRed')  
    lectureTurtle.drawPolygon(myTut, 100, 0,  50, 4, f_color='Lime')
    lectureTurtle.drawRectangle(myTut, -100, -100,  100, 50, f_color='blue')
    lectureTurtle.drawCircle(myTut, 0, -100,  50, f_color='Violet')   
    
    turtle.done()

main()