num = input("Choose a number to reverse:")
reversed_num = 0
saved_num = num
count = 0
while num >= 1:
   remainder = num % 10
   reversed_num  = reversed_num * 10 + remainder

   count = count + 1
   num = num / 10
if reversed_num == saved_num:
   print"%d is a palindrome" % (saved_num)
else:
   print "%d is not a palindrome" % (saved_num)


