# Draw a line from (x1, y1) to (x2, y2)
def drawLine(lecTurtle, x1, y1, x2, y2, b_color='black'):
    lecTurtle.color(b_color)
    lecTurtle.penup()
    lecTurtle.goto(x1, y1)    
    lecTurtle.pendown()
    lecTurtle.goto(x2, y2)

# Write a text at the specified location (x, y)
def writeText(lecTurtle, s, x, y, t_color='black'): 
    lecTurtle.color(t_color)
    lecTurtle.penup()
    lecTurtle.goto(x, y)
    lecTurtle.pendown()    
    lecTurtle.write(s)

# Draw a point at the specified location (x, y)
def drawPoint(lecTurtle, x, y, p_color='black'): 
    lecTurtle.color(p_color)
    lecTurtle.penup()
    lecTurtle.goto(x-1, y)
    lecTurtle.pendown()
    lecTurtle.begin_fill()    
    lecTurtle.circle(2) 
    lecTurtle.end_fill()

# Draw a circle at centered at (x, y) with the specified radius
def drawCircle(lecTurtle, x, y, radius, b_color='black', f_color=None ): 
    lecTurtle.color(b_color)
    lecTurtle.penup()
    lecTurtle.goto(x, y-radius)
    lecTurtle.pendown()
    
    if f_color != None:
        lecTurtle.fillcolor(f_color)
        lecTurtle.begin_fill()
        lecTurtle.circle(radius)
        lecTurtle.end_fill()
    else:
        lecTurtle.circle(radius) 
    
    # Draw a rectangle at (x, y) with the specified width and height
def drawRectangle(lecTurtle, x, y, width, height, b_color='black', f_color=None): 
    lecTurtle.color(b_color)
    lecTurtle.penup()    
    lecTurtle.goto(x+width/2, y+height/2)
    
    lecTurtle.pendown()
    lecTurtle.right(90)
    if f_color != None:
        lecTurtle.fillcolor(f_color)
        lecTurtle.begin_fill()
        lecTurtle.forward(height)
        lecTurtle.right(90)
        lecTurtle.forward(width)
        lecTurtle.right(90)
        lecTurtle.forward(height)
        lecTurtle.right(90)
        lecTurtle.forward(width)
        lecTurtle.end_fill()
    else:
        lecTurtle.forward(height)
        lecTurtle.right(90)
        lecTurtle.forward(width)
        lecTurtle.right(90)
        lecTurtle.forward(height)
        lecTurtle.right(90)
        lecTurtle.forward(width)
        
# Draw a polygon at centered at (x, y) with the specified radius
def drawPolygon(lecTurtle, x, y, radius, step, b_color='black', f_color=None): 
    lecTurtle.color(b_color)
    lecTurtle.penup()
    lecTurtle.goto(x, y-radius)
    lecTurtle.pendown()
    if f_color != None:
        lecTurtle.fillcolor(f_color)     
        lecTurtle.begin_fill()
        lecTurtle.circle(radius, steps=step) 
        lecTurtle.end_fill()
    else:
        lecTurtle.circle(radius, steps=step) 
        
    
def drawStar(lecTurtle, x, y, size=50, b_color='black'):
    lecTurtle.color(b_color)  
        
    lecTurtle.penup()
    lecTurtle.goto(x, y)    

    lecTurtle.pendown()
    lecTurtle.begin_fill()    

    for n in range(5):
        lecTurtle.forward(size)
        lecTurtle.right(144)
    
    lecTurtle.end_fill()     
    