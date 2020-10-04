import turtle
t = turtle.Pen()
def turn_around():
    t.right(180)
def stairs():
    for x in range(1,2):
        for x in range(1,5):
            t.forward(50)
            t.left(90)
            t.forward(50)
            t.right(90)
        turn_around()
        for x in range(1,4):
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.left(90)
        turn_around()

def main():
    t.right(90)
    for x in range(1,3):
        stairs()
        turn_around()
    raw_input("ENTER ANYHTING TO EXIT:")

if __name__ == "__main__":
    main()

