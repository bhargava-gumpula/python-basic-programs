file_name = raw_input("Enter a file name:")
f = open(file_name)
content = f.read()
print content
f.close()


