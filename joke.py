wrong = raw_input("what do you get when a queen farts?:")
while True:
    if wrong.upper() == "A NOBLE GAS":
       print ("You got it")
       break
    else:
       print ("Nope")
       wrong = raw_input("guess again")

