print ('''This is a matchstick game. 
You go first:''')
match_num = 21
while match_num > 1:
    user_num = input("Pick a number in these options: 1,2, 3 or 4:")
    if user_num > 4 or user_num < 1:
       print "invalid number"
    else:
       computer_pick = 5 - user_num
       print ("Computer picked : %d") % (computer_pick)
       match_num = match_num - (user_num + computer_pick)
       print ("Remaining sticks: %d") % (match_num)
    
if match_num == 1:
   print ('''HAHAHAHAHA, There is only 1 last matchstick left and you have to take it.
   you loose. better luck next time.''')    
