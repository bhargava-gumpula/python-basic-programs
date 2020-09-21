# Function to search a word in a list
def word_search(word_list, key):
   idx = 0 
   while idx < len(word_list):
      if key == word_list[idx]:
         return True 
      idx = idx + 1
   if idx == len(word_list):
     return False 

l = ["hi", "bhargava", "daddy", "mummy", "natasha", "games", "reading", "hobbys", "cool", "stuff"]
word = raw_input("enter any word:")
found = word_search(l, word)

if found:
   print ("%s is found in List") % (word)
else:
   print ("%s is not found in list") % (word)

