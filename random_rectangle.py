import random
from tkinter import*

tk = Tk()

def random_rectangle(width, height, color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2, fill=color)
    



canvas = Canvas(tk, height=500, width=500)
canvas.pack()
for x in range(0,100):
   random_rectangle(200,300, 'green')

raw_input("ENTER ANY KEY TO EXIT:")

