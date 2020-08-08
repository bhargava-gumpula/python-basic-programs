from tkinter import *
tk = Tk()
canvas = Canvas(tk, height=500, width=500)
canvas.pack()
canvas.create_arc(70,60,300,400, extent=90, style=ARC)

