months = {"January" : 31,
          "Febuary" : 28,
          "March" : 31,
          "April" : 30,
          "May" : 31,
          "June" : 30,
          "July" : 31,
          "August" : 31,
          "September" : 30,
          "October" : 31,
          "November" : 30,
          "December" : 31}


while True:
   month = raw_input("Choose Any Month:")
   if not month:
      print "invalid month"
      continue
   else: 
      print("There are %d days in %s") % (months[month], month)
      break

