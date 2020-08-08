num_friends = input ("How many friends do you have?:")

age_sum = 0
for x in range(1, num_friends + 1):
    friend_age = input ("What is you friends age?:")
    age_sum =  age_sum + friend_age
   
average_age = age_sum / num_friends
print ("The average age of you friends is %d") % (average_age)
   
