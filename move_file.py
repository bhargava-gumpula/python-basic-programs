import os

source_f = raw_input("ENTER A SOURCE FILE:")
dest_f = raw_input("ENTER A DESTINATION FILE:")
s = open(source_f, 'r')
d = open(dest_f, 'w')
content = s.readlines()
for line in content:
   d.write(line)

os.remove(source_f)
d.close()
