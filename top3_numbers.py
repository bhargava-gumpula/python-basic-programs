numbers = [100,20,39,48,53,62,72,85,96,10,24743,2482,238592]
second_large_num = 0
index = 0
max_num = numbers[0]
while index < len(numbers):
   
   if numbers[index] > max_num:
       thrid_last_num = second_large_num
       second_large_num = max_num
      
       max_num = numbers[index]
        
   
        
   index = index + 1
print thrid_last_num
print second_large_num
print max_num
