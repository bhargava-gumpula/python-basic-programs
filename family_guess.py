import random as r 
words = [mommy, daddy, me, akka]
secret_word = r.choice(words)
user_word = raw_input("Think of a word")
for x in range(1, 10):
   if user_word == secret_word:
      print ('''Your guess is correct
                congradulations''')
      break
   else:
      print ("No that is not correct")
print ("you lost the game")
