list1 = []
print "Before:"
print list1
print " "
list2 = []
num = len(list1)
while True:
   if num < 0:
      break
   list2.append(list1[num])
   num = num - 1
print "After:"
print list2

