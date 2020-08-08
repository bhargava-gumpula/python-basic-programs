def my_len(string):
   count = 0
   for letter in string:
       count = count + 1
   return count   


name = raw_input("ENTER YOUR NAME:")
l = my_len(name)
print "You have %s charectars in you name" % (l)
