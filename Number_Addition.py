import sys
number = input("Choose a start number:")
last_number = input("Choose a last number:")

if (number > last_number) :
    print ("INVAILID INPUT") 
    sys.exit()

sum = 0
num = number
while (number <= last_number):
    sum = number + sum
    number = number + 1
print ("The sum of numbers from %d to %d is %d") % (num,last_number,sum)
