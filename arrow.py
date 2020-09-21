from tkinter import *
tk = Tk()
canvas = Canvas(tk, height=500, width = 500)
canvas.pack()
tri_id = canvas.create_polygon(10, 10, 10, 60, 50, 35)
rect_id = canvas.create_rectangle(-30, 25, 10,45, fill="black")

for x in range(1, 75):
    canvas.move(tri_id, 5, 0)
    canvas.move(rect_id, 5, 0)
    tk.update()
raw_input("ENTER ANY KEY TO EXIT:")

