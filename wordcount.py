import sys

file_name = sys.argv[1]
f = open(file_name, 'r')
content = f.readlines()
num_words = 0
num_lines = 0

if len(sys.argv) > 3:
    print"please try again later"
    sys.exit()

for line in content:
    for word in line.split():
        num_words += 1
    num_lines +=1

if sys.argv[2].upper() == "words".upper():
    print "There are %d words in the file" % (num_words)

if sys.argv[2].upper() == "lines".upper():
    print "There are %d lines in the file" % (num_lines)
