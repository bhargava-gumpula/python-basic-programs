end_num = input("ENTER A NUMBER:")
l = [x for x in range(0,end_num)]
index = 0
sum_num = 0
while index < len(l):
   sum_num = sum_num + l[index]
   index = index + 1
print "the sum from 1 to you number = %s" % (sum_num)

