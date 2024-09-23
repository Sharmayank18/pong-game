from tkinter import * #import tk library
import random  # import random for random variable and time for delays
import time

#counter for player A and couter1 for player B
counter = 0
counter1 = 0

tk = Tk()
tk.title("Pong!")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
#canvas is an instance of the Canvas class from the Tkinter library
#which is used to draw shapes (circle,rectangle) and insert images
canvas = Canvas(tk, width = 500, height = 400, bd = 0 , 
highlightthickness = 0)
canvas.config(bg = "black")
canvas.pack()
tk.update()

canvas.create_line(250,0,250,400,fill = "white")
# game elements are a ball and hitpaddle for both player
class Ball:
  #A Ball class that handles the ball's movement, collision detection with paddles, and scoring.
  def __init__(self,canvas,color,paddle,paddle1):
    self.canvas = canvas
    self.paddle = paddle
    self.paddle1 = paddle1
    self.id = canvas.create_oval(10,10,25,25, fill=color)
    self.canvas.move(self.id, 235,200)
    starts = [-3,3]
    random.shuffle(starts)
    self.x = starts[0]
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = 500
 
  def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id)
    if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
      if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
        return True
      return False
 
  def hit_paddle1(self,pos):
    paddle_pos = self.canvas.coords(self.paddle1.id)
    #pos[0] is the x coordinate of top left corner
    #pos[1]: The y-coordinate of the top-left corner of the shape.
    #pos[2]: The x-coordinate of the bottom-right corner of the shape.
    #pos[3]: The y-coordinate of the bottom-right corner of the shape.
    if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
      if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
        return True
      return False
    
  def draw(self):
    self.canvas.move(self.id, self.x, self.y)
    pos = self.canvas.coords(self.id)
    if pos[1] <= 0:
      self.y = 3
    if pos[3] >= self.canvas_height:
      self.y = -3
    if pos[0] <= 0:
      self.x = 3
      self.score(True)
 
    if pos[2] >= self.canvas_width:
      self.x = -3
      self.score(False)
 
    if self.hit_paddle(pos) == True:
      self.x = 3
    if self.hit_paddle1(pos) == True:
      self.x = -3
  
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
 
 
 #A Paddle class for player 1 that responds to keyboard events (keys 'A' and 'D' for up and down movement).
class Paddle:
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id = canvas.create_rectangle(0,150,30,250, fill = color)
    self.y = 0
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()
    self.canvas.bind_all('a', self.turn_left)
    self.canvas.bind_all('d', self.turn_right)
 
  def draw(self):
    self.canvas.move(self.id, 0, self.y)
    pos = self.canvas.coords(self.id)
    if pos[1] <= 0:
      self.y = 0
    if pos[3] >= 400:
      self.y = 0
 
  def turn_left(self,evt):
    self.y = -3
 
  def turn_right(self,evt):
    self.y = 3

#A Paddle1 class for player 2 that responds to left and right arrow keys.
class Paddle1:
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id = canvas.create_rectangle(470,150,500,250, fill = color)
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()
    self.y = 0
    self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
    self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
  def draw(self):
    self.canvas.move(self.id, 0, self.y)
    pos = self.canvas.coords(self.id)
    if pos[1] <= 0:
      self.y = 0
    if pos[3] >= 400:
      self.y = 0
 
  def turn_left(self,evt):
    self.y = 3
 
  def turn_right(self,evt):
    self.y = -3

paddle = Paddle(canvas, "blue")
paddle1 = Paddle1(canvas, "pink")
ball = Ball(canvas, "orange", paddle, paddle1)

while 1:
  ball.draw()
  paddle.draw()
  paddle1.draw()
  if counter == 10:
    ball.x = 0
    ball.y = 0
    paddle.y = 0
    paddle1.y = 0
    canvas.create_text(250,200, text = "Congrats Player 1! You Win!", font = 32, fill = "red")
    canvas.create_text(250,215, text = "Score: " + str(counter) + " - " + str(counter1), font = 32, fill = "red")
  if counter1 == 10:
    ball.x = 0
    ball.y = 0
    paddle.y = 0
    paddle1.y = 0
    canvas.create_text(250,200, text = "Congrats Player 2! You Win!", font = 32, fill = "red")
    canvas.create_text(250,215, text = "Score: " + str(counter) + " - " + str(counter1), font = 32, fill = "red")
 
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)
  if counter == 10 or counter1 == 10:
    #s used to pause the execution of the program for a very long time (100,000 seconds, which is approximately 27.78 hours).
    time.sleep(100000)
 