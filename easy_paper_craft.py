import time
num = 1
l = ['one', 'thoo', 'thwee']
while True:
   if num == 4:
      time.sleep(1)
      print "EASY PAPER CRAFTS"
      break
   time.sleep(1)
   print num
   num = num + 1
num = 0
for x in range(num, len(l)):
   time.sleep(1)
   print l[num]
   num = num + 1
time.sleep(1)
print "Easy Paper Crafts!"

