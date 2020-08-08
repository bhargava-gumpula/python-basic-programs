# Program to sum series: 1^2 + 2^2 + 3^2 + 4^2 ....
num = input("Enter any number:")
total = 0
while num >= 0:
   total += (num * num)
   num = num - 1
print total
