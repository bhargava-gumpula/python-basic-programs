
def divide(dividend, divisor):
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
print ("%d / %d = %d | remainder = %d") % (dividend, divisor, groups, remainder)
