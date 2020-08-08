file_name = raw_input("ENTER A FILE NAME:")
word = raw_input("ENTER THE WORD YOU WANT IN THAT FILE:")

f = open(file_name, 'r')
content = f.readlines()

for line in content:
    if word in line:
      print line


f.close()
