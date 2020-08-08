user_num = input("Choose a number to reverse:")
reversed_num = 0

saved_num = user_num
count = 0
while user_num >= 1:
   remainder = user_num % 10 
   reversed_num = reversed_num * 10 + remainder
  
   count = count + 1
   user_num = user_num / 10


print reversed_num   
print ("Number of digits in %d is %d") % (saved_num, count)
  
