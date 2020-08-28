def seq_search(key, l):
    index = 0
    found = False
    while index <= len(l) - 1:
       if key == l[index]:
           found = True
           print "Found in list"
           break
       index += 1
    if not found:
        print " Not found in list"

l = [3,52,8,2356,25,7,7]
key = input("Enter a value to be searched:")
seq_search(key ,l)           
