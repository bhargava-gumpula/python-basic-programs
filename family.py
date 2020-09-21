family_age = {
              'BHARGAVA' : 9,
              'NATASHA' : 11,
              'MAMATHA' : 32,
              'SURESH' : 39
             }

name = raw_input("What is your name?:")
try:
   print ("Your age is %d") % (family_age[name.upper()])
except KeyError:
   print "Key Not in Map. Try Again Later. Bye"
