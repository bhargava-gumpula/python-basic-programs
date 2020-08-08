num = input("CHOOSE A NUMBER:")
saved_num = num 
fact = 1
while num >= 1:
   fact = fact * num 
   num = num - 1 

print ("Factorial of numer:%d is %d") % (saved_num, fact)
