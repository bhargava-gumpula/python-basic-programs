num = 1

while num <= 50:
   if num % 3 == 0 and num % 5 == 0:
      print "fizzbuzz"
   elif num % 5 == 0:
      print "buzz"
   elif num % 3 == 0:
      print "fizz"
   else:
      print num
   num = num + 1




