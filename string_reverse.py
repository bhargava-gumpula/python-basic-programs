user_word = raw_input("Enter any word:")
num = 1
str = ""
while num <= len(user_word):
   last_letter = user_word[-num]
   str = str + last_letter
   num = num + 1
print str
