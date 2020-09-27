import turtle
import time
t = turtle.Pen()

# Making outer box for grid
def draw_outer_box():
	t.forward(90)
	t.right(90)
	t.forward(90)
	t.right(90)
	t.forward(90)
	t.right(90)
	t.forward(90)
	t.right(90)

# Making horizontal lines for grid
def draw_horiz_lines():
	t.forward(30)
	t.right(90)
	t.forward(90)
	t.left(90)
	t.forward(30)
	t.left(90)
	t.forward(90)

# Making vertical lines for grid
def draw_verti_lines():
	t.right(90)
	t.forward(30)
	t.right(90)
	t.forward(30)
	t.right(90)
	t.forward(90)
	t.left(90)
	t.forward(30)
	t.left(90)
	t.forward(90)

# Making function for turning around
def turn_around():
    time.sleep(1)
    t.left(90)
    t.left(90)

# Making Plus sign
def draw_plus_sign():
	time.sleep(1)
	t.left(90)
	t.up()
	t.forward(90)
	t.down()
	t.forward(30)
	turn_around()
	t.forward(60)
	turn_around()
	t.forward(30)
	t.right(90)
	t.forward(30)
	turn_around()
	t.forward(60)
	turn_around()
	t.up()
	t.forward(120)
	t.down()

def main():
   draw_outer_box()
   draw_horiz_lines()
   draw_verti_lines()
   turn_around()
   draw_plus_sign()

if __name__ == "__main__":
    main()

# Asking user to exit
raw_input("Enter anything to exit:")

