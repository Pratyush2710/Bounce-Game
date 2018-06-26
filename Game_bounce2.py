from tkinter import*
import random
import time

root = Tk()
root.title("Bounce Game")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = Canvas(root, height = 500, width = 500, bd = 0, highlightthickness =0)
canvas.pack()
root.update()



class Ball:
    
    def __init__(self,canvas,paddle,color):
        self.paddle = paddle
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill =color)
        self.canvas.move(self.id, 400,400)
        start = [-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        
    def hit_paddle(self,pos):
         paddle_pos = self.canvas.coords(self.paddle.id)
         
         #pos contains coordinate of ball
         # pos[2] contains right side of ball and paddle_pos[0] left side of paddle 
         if pos[2]>= paddle_pos[0] and pos[0]<= paddle_pos[2]:
             if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                 return True
             return False
    
    
    def draw(self):
        self.canvas.move(self.id, self.x,self.y)
        pos = self.canvas.coords(self.id)    # give x1[0] , y1[1] , x2[2] , y2[3]
        print(pos)
        if pos[1]<=0:
            self.y = 1
        if pos[3]>= self.canvas_height:
            self.hit_bottom = True 
            canvas.create_text(245,100,text="GAME OVER")
        if pos[0] <=0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2
        if self.hit_paddle(pos) == True:
            self.y = -2
        
        
    

        
class Paddle:
    
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill = color)
        self.canvas.move(self.id, 200,300)
        self.x = 0
        self.canvas_width = self. canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        
    def draw(self):
        self.canvas.move(self.id, self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x =0

    def turn_left(self,event):
        self.x = -2

    def turn_right(self,event):
        self.x = 2
    
    

paddle = Paddle(canvas,"blue")
ball = Ball(canvas,paddle, "red")



while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.001)
    
    
    
    
    



