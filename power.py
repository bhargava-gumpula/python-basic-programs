
# Function to find the power of x^y
def power(x,y):
   temp = 1
   while y >= 1:
      temp = temp * x
      y = y - 1

   return temp

num1 = input("Enter base number:")
num2 = input("Enter power number:")

result = power(num1,num2)
print ("%d to the power of %d is %s") % (num1, num2, result)                                             
