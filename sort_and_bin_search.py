def bubble_sort(l):
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
          break
        index2 += 1       

def binary_search(l,key):
    high = len(l)
    found = False
    low = 0
    while low < high:
       mid = (high + low) / 2
       if key == l[mid]:
         found = True
         print ("found in list")
         break
       if key > l[mid]:
        low = mid + 1
       else:
         high = mid  - 1
    if not found:
       print "Not found in list"  

def main():
    l = [42,5,6,8,5,1,57,25]
    key = input("Enter a number you want to find in a list:")

    bubble_sort(l)
    binary_search(l,key)

if __name__ == "__main__":
    main()


