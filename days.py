leap_year = raw_input("Is it a leap year? y/n:")
Feb = None
if leap_year.upper() == "Y":
    Feb = 29
if leap_year.upper() == "N":
    Feb = 28

days = [31,Feb,31,30,31,30,31,31,30,31,30,31]
month = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'August', 'Sep', 'Oct', 'Nov', 'Dec']
print ("Month\tdays")
print ("===============")
sum = 0 
x = 0
while x < 12:
    sum = sum + days[x]
    print ("%s\t %d   ") % (month[x], days[x])
    x = x + 1

print "================"
print ("Total  =   %d") % (sum)



























