import sys
num = input("Enter any number:")

if (num == 1):
  print "Not a prime"
  sys.exit()

if (num == 2):
  print "Prime number"
  sys.exit()

for i in range(2, num):
   if (num % i) == 0:
        print("not prime number")
        break

if (i + 1) == num:       
   print "prime number"
       
