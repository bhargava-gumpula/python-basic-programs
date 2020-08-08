# Pong Game
# Author: Bhargava Gumpula
# Start Date: 07/19/2020
# End Date: ??/??/2020

from tkinter import*
import time
import random
import sys

# Ball class handles ball movement
class Ball:
    def __init__(self, radius, color, canvas, paddle, x = 500, y = 200):
      # how much to move
      starts = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
      self.rand_x = starts[0]
      self.rand_y = -5
      self.paddle = paddle
      self.canvas = canvas
      self.radius = radius
      self.color = color
      random.shuffle(starts)

      self.points = 0
      # Ball position
      self.x = x
      self.y = y
      self.id = self.canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill=self.color)
      self.canvas_height = canvas.winfo_height()
      self.canvas_width = canvas.winfo_width()
        
    def draw(self):
          hit = False
          # Check if touching the paddle
          if (self.x <= self.paddle.x2 and self.x >= self.paddle.x1) and \
              (self.y + self.radius) == self.paddle.y1:
             self.points = self.points + 1
             self.rand_y = self.rand_y - 15
         
          # Check if ball touching right edge of the canvas    
          if (self.x + self.radius) >= 1000:
             self.rand_x = self.rand_x - 15
             hit = True
          elif (self.x - self.radius) <= 0:
             self.rand_x = self.rand_x + 15
             hit = True
          # Check if ball touching the bottom of the canvas
          elif (self.y + self.radius) >= 780:
             temp_str = "Game Over, Points = %d, wait for 3secs to start" % (self.points)
             text_id=self.canvas.create_text(500,500,text=temp_str, font=('Couier',30))
             tk.update()
             time.sleep(3)
             canvas.delete(text_id)
             self.points = 0
             self.rand_y = self.rand_y - 15
          # checking if ball touching top canvas
          elif (self.y - self.radius) <= 0:
             self.rand_y = self.rand_y + 15
             hit = True
            
          self.canvas.move(self.id,self.rand_x, self.rand_y)

          self.x = self.x + self.rand_x
          self.y = self.y + self.rand_y
          
             
# Paddle class handles paddle movement and bouncing the ball
class Paddle:
   def __init__(self, canvas, speed = 70):
      self.speed = speed
      self.x1 = 400
      self.y1 = 700
      self.x2 = 550
      self.y2 = 730
      self.canvas = canvas
      
   def movepaddle(self,event):
         if event.keysym == 'Left':
           if (self.x1 >= self.speed):
              self.x1 =  self.x1 - self.speed
              self.x2 = self.x2 - self.speed
              self.canvas.move(self.paddle ,-self.speed,0)
         if event.keysym == 'Right':
           if (self.x2 <= 950 - self.speed):
              self.x2 =  self.x2 + self.speed
              self.x1 = self.x1 + self.speed
              self.canvas.move(self.paddle ,self.speed,0)
         if event.keysym == 'Down':
            sys.exit()
   def draw(self):
      self.paddle = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='blue')
      
      self.canvas.itemconfig(self.paddle, outline = 'black')

def end_game(event):
   sys.exit()

tk = Tk()
def game_start():
  red_ball = Ball(20, 'red', canvas, paddle)
  while True:
    red_ball.draw()
    tk.update_idletasks()
    tk.update()

# Main program
tk.title("Pong Game")

# Draw the canvas
canvas = Canvas(tk, height=1000, width=1000)
canvas.pack()

# Draw the Paddle
paddle = Paddle(canvas)
paddle.draw()
canvas.bind_all('<Key-Right>', paddle.movepaddle)
canvas.bind_all('<Key-Left>', paddle.movepaddle)
canvas.bind_all('<Key-Down>', paddle.movepaddle)

game_start()
raw_input("PRESS ANY KEY TO EXIT:")

