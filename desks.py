tables = input ("How many tables are in total:")
students = input ("How many students are at each table:")
total = int(tables) * int(students)

if total >= 2:  
    print "There are %d students in all" % (total)
elif total == 1: 
    print  "There is %d student only!" % (total)
else:
     print "There are no students at all"
