table_number = input ("Choose a multiplication table:")
multipls = input ("How many multipls do you want:")

num = 1 
while num <= multipls:
    product = table_number * num
    print ("%d * %d = %d") % (table_number, num, product)
    num = num + 1 
print "DONE"

