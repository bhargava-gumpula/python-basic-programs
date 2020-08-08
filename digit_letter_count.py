import re

def is_letter(letter):
   if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
      return True
   else:
      return False

def is_number(number):
   if number >= '0' and number <= '9':
     return True
   else:
     return False


letters = 0
numbers = 0
string = raw_input("ENTER ANYTHING OF YOUR KEYBOARD:")
for x in range(0, len(string)):
   if is_letter(string[x]): 
      letters = letters + 1
   if is_number(string[x]):
      numbers = numbers + 1
      
print "There are %d letters in %s" % (letters, string)
print "There are %d numbers in %s" % (numbers, string)
