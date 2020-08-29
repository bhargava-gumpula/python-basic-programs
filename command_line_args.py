import sys

# Check if he is giving more than expected parameters
if (len(sys.argv) - 1) > 2:
    print ("NEED ONLY 2 PARAMETERS")
    sys.exit()

# Index 0 is the file name, so we have to start from index 1
index = 1
while index < len(sys.argv):
    print sys.argv[index]
    index = index + 1

