def binary_search(l, key):
    low = 0
    high = len(l) 
    found = False

    while low < high:
        mid = (high + low) / 2
        if key == l[mid]:
            found = True
            print ("found in list")
            break
        if key > l[mid]:
           low = mid + 1
        else:
           high = mid - 1

    if not found:
       print "Not found in list"
    
l = [1,2,3,4,5,6,7,8,9,10]
key = input("ENTER ANY NUMBER YOU WANT TO FIND IN A LIST:")
binary_search(l, key)
