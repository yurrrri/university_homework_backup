import turtle

imageList = {"left":"robot_Leftward.gif", "right":"robot_Rightward.gif", 
             "up":"robot_Upward.gif", "down":"robot_Downward.gif", }

class Window:
    def __init__(self, robot):
        self.robot= robot
        self.screen = turtle.Screen()
        self.screen.setup(750, 750)
                
        self.screen.onkey(self.upward, "Up")
        self.screen.onkey(self.downward, "Down")
        self.screen.onkey(self.rightward, "Right")
        self.screen.onkey(self.leftward, "Left")

    def setDefaultImage(self):
        self.robot.robotPen.shape(imageList["left"])    
    
    def upward(self):
        self.robot.robotPen.setheading(90)         
        self.robot.robotPen.shape(imageList["up"])
        self.robot.robotPen.forward(50)

    def downward(self):        
        self.robot.robotPen.setheading(270)         
        self.robot.robotPen.shape(imageList["down"])
        self.robot.robotPen.forward(50)  

    def leftward(self):       
        self.robot.robotPen.setheading(180)         
        self.robot.robotPen.shape(imageList["left"])
        self.robot.robotPen.forward(50)
      
    def rightward(self):
        self.robot.robotPen.setheading(0)         
        self.robot.robotPen.shape(imageList["right"])
        self.robot.robotPen.forward(50)

class Robot:
    def __init__(self):
        self.robotPen = turtle.Turtle()
        #self.robotPen.penup()
        
def main():    
    robot = Robot()
    win = Window(robot)    

    for im in imageList:
        win.screen.addshape(imageList[im])  
    
    win.setDefaultImage()    
    
    win.screen.listen()
    win.screen.mainloop()
        
    #turtle.done()
    
main()