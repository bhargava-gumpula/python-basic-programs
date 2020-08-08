temp = raw_input("Enter the temperature:")

degree = int(temp[:-1])
symbol = temp[-1]

if symbol.lower() == "c": 
   value = (9 * degree) / 5 + 32
   print ("The converted temperature is %dF") % (value)
elif symbol.lower() == "f":
   value = (degree - 32) *  5.0 / 9 
   print ("The converted temperature is %dC") % (value)
else:
    print("Invalid temperature")



