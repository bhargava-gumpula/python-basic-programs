# This code takes the input of a roman numeral and gives you the coresponding number

rNumeral = input("What Numeral Do you Want to Covert : ")
numerals = {"I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000}
total = 0

# We use - 1 in the for loop because we have to check the next number to see to subtract. If we add 1 then the index will go   out of range

for i in range (len(rNumeral) - 1):
    # These next two if statments are for checking if we have to subtract

    if rNumeral[i] == "I" and rNumeral[i + 1] == "V":
        total = total + 4
        i = i + 1
        continue
    if rNumeral[i] == "I" and rNumeral[i + 1] == "X":
        total = total + 9
        i = i + 1
        continue

    # if both false it just adds the number	
    total = total + numerals[rNumeral[i]]

# When we do - 1 in the for loop it does not go to the last index so we have to add it by using i + 1
total = total + numerals[rNumeral[i+1]]    

# Then we show our answer
print (total)
