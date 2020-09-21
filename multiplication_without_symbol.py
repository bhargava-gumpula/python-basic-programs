def multiplication(factor1, factor2):
   temp_int = 1
   saved_factor = factor1
   while temp_int < factor2:
      factor1 += saved_factor
      temp_int += 1
   return factor1
 
factor1 = input("ENTER FIRST FACTOR:")
factor2 = input("ENTER LAST FACTOR:")
result = multiplication(factor1, factor2)
print ("%d * %d = %d") % (factor1, factor2, result)
