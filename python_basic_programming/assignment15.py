#-*- coding:utf-8 -*-

'''
학번: 20161048 이름:이유리
과제번호: 과제  15
제출일자: 2016.12.09
'''

import tkinter as tk
import random

brickData = {'col':12, 'row':6, 'width':50, 'height':25, 'color1':'saddlebrown','color2':'rosybrown'}
paddleData = {'color':'white', 'width':90, 'height':10, 'speed':23}
ballData = {'color': 'red', 'size':30}


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

class PlayingFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack()
        
        self.shapeobjects = {}
        
        self.count = 0
        self.score = tk.Label(self, text='격파 블록 수: ' + str(self.count), padx=10, pady=10)
        self.score.pack()
        
        self.playground = tk.Canvas(self, background='black', width=600, height=550)
        self.playground.pack()
        
        self.boundary = None
        self.brick = None
        self.paddle = None
        self.ball = None
        
    def startgame(self):
        self.shapeobjects = {}
        
        self.playground.delete(tk.ALL)
        self.count=0
        self.score.config(text='격파 블록 수: ' + str(self.count))
        
        self.boundary = Boundary(self)
        self.brick = Brick(self)
        self.paddle = Paddle(self)
        self.ball = Ball(self)
    
        self.bind('<Left>', self.arrowKeyPressed)
        self.bind('<Right>', self.arrowKeyPressed)
        self.focus_set()
    
        flag = False
        
        while not flag:
            self.moveball()
            flag = self.checkoverlap()

    def arrowKeyPressed(self, event):
        if event.keysym == 'Left' and self.paddle.position['x']>=5 :
            paddleData['speed'] = -5
        elif event.keysym=='Right' and self.paddle.position['x']+paddleData['width'] <= 595 :
            paddleData['speed'] = 5
        else :
            paddleData['speed'] = 0
            
        self.paddle.position['x'] += paddleData['speed']
        self.playground.move('paddle', paddleData['speed'], 0)
        self.playground.update()
            
    def moveball(self):
        self.playground.move('ball', self.ball.dx, self.ball.dy)
        self.playground.after(23)
        self.playground.update()

    def checkoverlap(self):
        endflag = False
    
        tmp = self.playground.coords(self.ball.gameball)
        
        x1=tmp[0]
        y1=tmp[1]
        x2=tmp[2]
        y2=tmp[3]
        
        overlapped_list = self.playground.find_overlapping(x1, y1, x2, y2)
        
        for k,v in self.shapeobjects.items():
            if v in overlapped_list:
                if k=='paddle' or k=='wallup':
                    self.ball.dy=-self.ball.dy
                elif k=='wallleft' or k=='wallright':
                    self.ball.dx=-self.ball.dx
                elif k=='walldown' or k=='leftdown' or k=='rightdown':
                    self.playground.delete(tk.ALL)
                    self.playground.create_text(300, 300, font=('Arial', 14), text='Game Over!!',fill='red', justify=tk.CENTER)
                    endflag = True
                else:
                    self.ball.dy=-self.ball.dy
                    self.playground.delete(self.shapeobjects[k])
                    self.count+=1
                    self.score.config(text='격파 블록 수: ' + str(self.count))
                    
                    if len(self.shapeobjects.keys())==7:
                        endflag=True
                        
        return endflag

class Boundary:
    def __init__(self, frame):
        self.position=[['wallup',0,0,600,2],['walldown',0,548,600,550],['wallleft',0,2,2,500],['wallright',598,2,600,500],['leftdown',0,500,2,548],['rightdown',598,500,600,548]]
        
        for n in self.position:
            frame.shapeobjects[n[0]]=frame.playground.create_rectangle(n[1],n[2],n[3],n[4])

class Brick:
    def __init__(self, frame):
        for x in range(brickData['col']):
            for y in range(brickData['row']+1):
                name = 'brick'+str(x) + str(y)
                startpoint = [x*brickData['width'], 50+y*brickData['height']]
                endpoint = [(x+1)*brickData['width'], 50+(y+1)*brickData['height']]
                if (x+y)%2 == 0 :
                    frame.shapeobjects[name] = frame.playground.create_rectangle(startpoint[0],
                                                                                 startpoint[1], endpoint[0], endpoint[1],outline='black', fill=brickData['color1'])
                else :
                    frame.shapeobjects[name] = frame.playground.create_rectangle(startpoint[0],startpoint[1], endpoint[0], endpoint[1],outline='black', fill=brickData['color2'])
class Paddle:
    def __init__(self, frame):
        self.position = {'x':250, 'y':538} #패들과 공이 만날 때 바르르 떠는 현상:paddle의 시작 위치를 전보다 높이기 위해 paddle의 startpoint y값을 2픽셀 만큼 줄임 (540-2)
        frame.shapeobjects['paddle'] = frame.playground.create_rectangle(self.position['x'],
                                                                         self.position['y'],
                                                                         self.position['x']+paddleData['width'],
                                                                         self.position['y']+paddleData['height'],fill = paddleData['color'], tag='paddle')
class Ball:
    def __init__(self, frame):
        self.position = {}
        self.position['x'] = random.randint(35, 565)
        #공이 오른쪽이나 왼쪽에서 나왔을 때 파르르 떠는 현상:
        #원 프로그램에서 random.randint(0,600)을 하면, x좌표의 범위가 0부터 599까지인데 만약에 x좌표가 0,1,2거나 598,599로 설정된다고 가정하면 왼쪽, 오른쪽 벽의 범위에 포함되는 것이므로 그 사이에서 계속 튕기는 것임. 그래서 공의 size와 벽의 크기를  고려하여 randint 범위 변경
        
        self.position['y'] = 231

        self.dx = 5 ; self.dy = 5   
        self.gameball = frame.playground.create_oval(self.position['x'], self.position['y'],
                                                self.position['x']+ballData['size'],
                                                self.position['y']+ballData['size'],
                                                fill = ballData['color'], tag='ball')
class ControlFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.parent = parent

        self.playBtn = tk.Button(self, text='시 작', width=10, pady=5,
                                 command=self.parent.playingFrame.startgame)
        self.playBtn.pack(side=tk.LEFT)
        
        self.exitBtn = tk.Button(self, text='종 료', width=10, pady=5, command=self.parent.quit)
        self.exitBtn.pack(side=tk.LEFT)
        
def main():
    
    myapp = BrickApp()
    myapp.mainloop()
    
main()