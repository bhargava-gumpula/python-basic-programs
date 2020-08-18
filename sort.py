def find_index(key, list_name):
      index = 0
      while index <= len(list_name): 
         if list_name[index] == key:
             return index
         index += 1         
 
def sort_list(l1):
       order = []
       for x in range(0,len(l1)):
            min_num = min(l1)
            order.append(min_num)
            index = find_index(min_num, l1)
            del l1[index]
       return order
 
list_order = [10,9,3,5,7,4,1,2,8,6]
sorted_list = sort_list(list_order)
print sorted_list
