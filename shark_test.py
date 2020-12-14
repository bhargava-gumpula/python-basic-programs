def shark_test(size, color):
    if size == "large":
        if color == "gray":
            print("Look out for sharks!")
        else: 
            print("Do you see a whale?")
    else:
        if color == "orange":
            print("You probably own a goldfish.")
        else:
            print("Your fish could be tropical.")

size = raw_input("What is the size:")
color = raw_input("What is the color:")
shark_test(size, color)
