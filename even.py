import custom_functions as cf

number = input ("enter a number:")
if cf.even(number):
    print "The number %d is even!" % (number)
elif cf.odd(number):
    print "The number %d is odd!" % (number)
     
