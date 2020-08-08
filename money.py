# This is a are you rich program

# First we have to ask the user for a integer
money = input ("How much money do you have:")
if_job = raw_input("Do you have a job?:")

if if_job.upper() == "YES":
   if money > 3000:
      print ("You have a good job")
   elif money == 3000:
      print ("You are a normal person")
   elif money >= 0:
      print ("Try getting a new job")

if if_job.upper() == "NO":   
   if money > 3000:
      print ("You have alot of money")
   elif money == 3000:
      print ("You are a normal person")
   elif money >= 0:
      print ("Try earning more money")
 
