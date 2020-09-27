from tkinter import *
canvas = Canvas(height = 200, width = 500)
c = colorchooser.askcolor()
canvas.create_rectangle(0,0,500,20,outline="Green", fill=c[1])
canvas.pack()
canvas.update()
raw_input("Enter Any key to exit:")
