l = [1,2,3,4,6,7]
index2 = 0
sorted = True
while index2 < len(l) - 1:
    index = 0
    while index < len(l) - 1 - index2:
        if l[index] > l[index + 1]:
            saved_num = l[index]
            l[index] = l[index + 1]
            l[index + 1] = saved_num 
            sorted = False
        index = index + 1

    if (sorted):
      print "THIS WAS PRESORTED"  
      print l
      break
    else:
       print l
    index2 += 1        
