import custom_functions as cf

def print100():
   num=1
   while (num <=100):
     print num
     num = num + 1

num = 100
string = " "
while num <= 400:
   if (cf.even(num)):
      string = string + str(num) + ", "

   num = num + 1
print string

