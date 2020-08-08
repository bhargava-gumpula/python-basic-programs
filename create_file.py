import sys
file_name = raw_input("ENTER A FILE NAME:")
f = open(file_name,'w')
print("ENTER YOU FILE CONTENT LINE BY LINE AND AT THE END PRESS ENTER")
while True:
   line = raw_input()
   if line:
     f.write(line)
   else:
      f.write("\n")
      break

print "YOUR FILE HAS BEEN CREATED"
f.close()   
