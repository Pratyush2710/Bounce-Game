from tkinter import *
import random
import time

counter = 0
counter1 = 0
x=True
root = Tk()
root. title("PONG")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = Canvas(root, width = 500, height = 500, bd =0, highlightthickness = 0)
canvas.config(bg = "black")


canvas.pack()
root.update()

canvas.create_line(250,0,250,500,fill ="white")



class Ball:
    def __init__(self,canvas,color, paddle, paddle1):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle1 = paddle1
        self.id = canvas.create_oval(10,10,25,25, fill =color)
        self.canvas.move(self.id, 235,250)
        start =[-3,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        if counter ==2 or counter1 ==2:
            start=0
            self.x=0
            self.y=0
        


   
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y = 3
        if pos[3]>= self.canvas_height:
            self.y = -3
        if pos[0]<=0:
            self.x = 3
            self.score(True)
            
        if pos[2]>= self.canvas_width:
            self.x =-3
            self.score(False)
            
            
        if self.hit_paddle(pos) == True:
            self.x =3
        if self.hit_paddle1(pos) == True:
            self.x = -3
        
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            # 1 if posiiton[1] top part of ballis under top part of paddle and bottom of paddle[3]
            
            if pos[0]>=paddle_pos[0] and pos[0]<= paddle_pos[2]: 
                #left side of ball 0 is more than left side of paddle[0] and between right part of paddle
                return True
            return False
      
    def hit_paddle1(self,pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]: # 1 if posiiton[1] top part of ballis under top part of paddle and bottom of paddle[3]
            
            if pos[2]>=paddle_pos[0] and pos[2]<= paddle_pos[2]: #left side of ball 0 is more than left side of paddle[0] and between right part of paddle
                return True
            return False
 
   
    
    
    
    
    
    
    def score(self, val):
        global counter
        global counter1
        
        if val == True:
            a = self.canvas.create_text(125,40, text = counter, font = ("Arial", 60), fill = "white")
            canvas.itemconfig(a,fill = "black")
            counter += 1
            a = self.canvas.create_text(125,40, text = counter, font = ("Arial", 60), fill = "white")
            
        if val == False:
            a = self.canvas.create_text(375,40, text = counter1, font = ("Arial", 60), fill = "white")
            canvas.itemconfig(a,fill = "black")
            counter1 += 1
            a = self.canvas.create_text(375,40, text = counter1, font = ("Arial", 60), fill = "white")
        
   
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,150,30,250, fill = color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('a', self.turn_left)
        self.canvas.bind_all('d' , self.turn_right)
    def draw(self):
        self.canvas.move(self.id, 0 , self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y = 0
        if pos[3]>=500:
            self.y = 0
            
    def turn_left(self,evt):
        self.y = -5
    def turn_right(self,evt):
        self.y = 5
   
class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(470,150,500,250, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y =0
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        
    def draw(self):
        self.canvas.move(self.id, 0 , self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y = 0
        if pos[3]>=500:
            self.y = 0
    
    def turn_left(self,evt):
        self.y = 5
    
    def turn_right(self,evt):
        self.y = -5
       

paddle = Paddle(canvas,"blue")
paddle1 = Paddle1(canvas, "red")
ball = Ball(canvas,"yellow",paddle, paddle1)

while x == True:
    ball.draw()
    paddle.draw()
    paddle1.draw()
    
    
    if counter == 2:
        ball.x=0
        ball.y=0
        paddle.y=0
        paddle1.y=0
        canvas.create_text(250,250,text="Congrats Player1 ! You Win!", font = 32, fill="white")
        canvas.create_text(250,125,text="Score:"+ str(counter)+" - "+str(counter1), font = 32, fill="red")
    
    if counter1 == 2:
        ball.x=0
        ball.y=0
        paddle.y=0
        paddle1.y=0
        canvas.create_text(250,250,text="Congrats Player2 ! You Win!", font = 32, fill="white")
        canvas.create_text(250,125,text="Score:"+ str(counter)+" - "+str(counter1), font = 32, fill="red")
           
    root.update_idletasks
    root.update()
    time.sleep(0.01)
    
    if counter ==2 or counter1 ==2:
        time.sleep(10000)