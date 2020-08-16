def divide(dividend, divisor):

   if divisor == 0:
     return (dividend, -1)

   groups = 0
   while True:
      if divisor > dividend:
         remainder = dividend
         break
      dividend -= divisor
      groups += 1
   return remainder, groups
 
dividend = input("Enter Dividend:")
divisor = input("Enter Divisor:")
remainder, groups = divide(dividend, divisor)

if groups == -1:
  print ("%d / %d = undefined") % (dividend, divisor)
else:
  print ("%d / %d = %d | remainder = %d") % (dividend, divisor, groups, remainder)
#===============================================================================================
def divide(dividend, divisor):
   if divisor == 0:
      return dividend, -1
   groups = 0
   while divisor <= dividend:
      dividend -= divisor
      groups += 1
   reaminder = dividend  
   return reaminder, groups

dividend = input("Enter Dividend:")
divisor = input("Enter Divisor:")
remainder, groups = divide(dividend, divisor)
if groups == -1:
  print ("%d / %d = undefined") % (dividend, divisor)
else:
  print ("%d / %d = %d | remainder = %d") % (dividend, divisor, groups, remainder)

