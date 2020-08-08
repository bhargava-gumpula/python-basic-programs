import turtle
import time

class Car:

   def __init__(self, t):
      self.t = t

   def draw_tire(self):
      self.t.color(0,0,0)
      self.t.begin_fill()
      self.t.circle(20)
      self.t.end_fill()

   def top_shape(self):
      self.t.color(1,0,0)
      self.t.begin_fill()
      self.t.forward(130)
      self.t.left(90)
      self.t.forward(50)
      self.t.left(90)
      self.t.forward(50)
      self.t.right(90) 
      self.t.forward(50)
      self.t.left(90)
      self.t.forward(50)
      self.t.left(90)
      self.t.forward(50)
      self.t.right(90)
      self.t.forward(50)
      self.t.left(90)
      self.t.forward(50)
      self.t.end_fill()

   def draw(self):
     self.top_shape()
     self.t.up()
     self.t.forward(20)
     self.t.down()
     self.draw_tire()

     self.t.up()
     self.t.backward(20)
     self.t.down()
  
     self.t.left(90)
     self.t.up()
     self.t.forward(130)
     self.t.down()
     self.t.right(180)
     self.draw_tire()     

t1 = turtle.Pen()
car1 = Car(t1)
t2 = turtle.Pen()
car2 = Car(t2)


t2.up()
t2.left(90)
t2.forward(100)
t2.down()
t2.right(90)

move_c1 = 10
move_c2 = 10

for x in range(1,100):
  car1.draw()
  car2.draw()
  t1.reset()
  t2.reset()
  t1.up()
  t1.forward(move_c1)
  t1.down()
  move_c1 = move_c1 + 30


raw_input("ENTER ANY KEY TO EXIT:")

