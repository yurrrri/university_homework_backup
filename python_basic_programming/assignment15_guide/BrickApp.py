#-*- coding:utf-8 -*-

import tkinter as tk

brickData = {'x':12, 'y':6, 'width':50, 'height':25, 'color1':'saddlebrown', 'color2':'rosybrown'}
paddleData = {'width':90, 'height':10, 'position':[6, 19], 'speed':5}
ballData = {'color': 'red', 'size':30, 'speed':3}

class BrickApp(tk.Tk):
    def __init__(self):        
        tk.Tk.__init__(self)        
        
        self.geometry('700x650')
        self.resizable(width=False, height=False)
        self.title('블록 깨기')
        
        self.playingFrame = PlayingFrame(self)    
        self.playingFrame.pack()
             
        self.controlFrame = ControlFrame(self)
        self.controlFrame.pack()
        
        self.playingFrame.startGame()
        
class PlayingFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack()
        #self.parent = parent 

        self.count = 0 
        self.score = tk.Label(self, text='블록 갯수  : '+ str(self.count), padx=10, pady=10)
        self.score.pack()
        
        self.playground = tk.Canvas(self, background='black', width=600, height=550)
        self.playground.pack()
        
        self.brick = Brick(self)
        self.paddle = Paddle(self)
        self.ball = Ball(self)          

    def startGame(self):
        self.dx=0 ;   self.dy=0
                    
        self.bind('<Left>', self.arrowKeyPressed)
        self.bind('<Right>', self.arrowKeyPressed)
        self.bind('<space>', self.initGame)
        self.focus_set()               
        
        while True:
            self.moveball()
        
    def arrowKeyPressed(self, event):        
        if event.keysym == 'Left' and self.paddle.position['x']>=5 :
            paddleData['speed'] = -5            
        elif event.keysym=='Right' and self.paddle.position['x']+paddleData['width'] <= 595 :
            paddleData['speed'] = 5 

        self.paddle.position['x'] += paddleData['speed']   
        self.playground.move('paddle', paddleData['speed'], 0)
        self.playground.update()    

    def initGame(self, event):
        if self.ball.position['x']+ballData['size']//2 > self.paddle.position['x']+paddleData['width']//2 :
            self.dx = ballData['speed']
        elif self.ball.position['x']+ballData['size']//2 < self.paddle.position['x']+paddleData['width']//2 :
            self.dx = -ballData['speed']
        else :
            self.dx = 0        
        self.dy = -ballData['speed']

        self.ball.position['x'] += self.dx
        self.ball.position['y'] += self.dy     
           
        self.playground.move('ball', self.dx, self.dy)
        self.playground.after(10)
        self.playground.update() 
        
    def moveball(self):
        rightBound = 600 - ballData['size']
        bottomBound = 550
        newX = self.ball.position['x'] + self.dx 
        newY = self.ball.position['y'] + self.dy      
        
        if newX<0 :
            self.ball.position['x'] = 0
            self.dx = -self.dx            
        elif newX>rightBound :
            self.ball.position['x'] = rightBound
            self.dx = -self.dx
        else :
            self.ball.position['x'] = newX
            
        if newY<0 :
            self.ball.position['y'] = 0
            self.dy = -self.dy            
        elif newY>bottomBound :
            self.score['text'] = 'Game Over!'    
            
        else :
            self.ball.position['y'] = newY

        self.playground.move('ball', self.dx, self.dy)
        self.playground.after(10)
        self.playground.update() 
        

class Brick:    
    def __init__(self, frame):     
        self.frame = frame   
        self.brickList = []
        self.width = brickData['width']
        self.height = brickData['height']
        
        for x in range(brickData['x']):
            for y in range(1, brickData['y']+1):
                self.brickList.append([x, y])
                if (x+y)%2 == 0 :
                    self.frame.playground.create_rectangle(x*brickData['width'], y*brickData['height'],
                                             (x+1)*brickData['width'], (y+1)*brickData['height'],
                                             fill = brickData['color1'], outline='black')    
                else :
                    self.frame.playground.create_rectangle(x*brickData['width'], y*brickData['height'],
                                             (x+1)*brickData['width'], (y+1)*brickData['height'],
                                             fill = brickData['color2'], outline='black')    

class Paddle:
    def __init__(self, frame):
        self.position = {'x':250, 'y':530}
        self.width = paddleData['width']
        self.height = paddleData['height']
        
        self.frame= frame      
        self.frame.playground.create_rectangle(self.position['x'], self.position['y'],
                                               self.position['x']+paddleData['width'], self.position['y']+paddleData['height'],                                                                                           
                                                fill = 'white', tag='paddle')

class Ball:
    def __init__(self, frame):        
        self.frame = frame
        self.position = {'x': self.frame.paddle.position['x']+30, 'y':self.frame.paddle.position['y']-30}
        '''
        ballimage = tk.PhotoImage(file='ball.gif')
        self.frame.playground.create_image(self.position['x'], self.position['y'], image=ballimage, tag='ball')
        '''
        self.frame.playground.create_oval(self.position['x'], self.position['y'],
                                          self.position['x']+ballData['size'], self.position['y']+ballData['size'],                                                                                           
                                          fill = ballData['color'], tag='ball')
        

class ControlFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent 
        
        self.playBtn = tk.Button(self, text='시 작', width=10, pady=5, command=self.parent.playingFrame.startGame)
        self.playBtn.pack(side=tk.LEFT)
        
        self.exitBtn = tk.Button(self, text='종 료', width=10, pady=5, command=self.parent.quit)
        self.exitBtn.pack(side=tk.LEFT)
        
def main():    
    myapp = BrickApp()
    myapp.mainloop()

main()