lines = []

print "Enter multiple lines and press \"Enter\" to terminate"
while True:
  l = raw_input()
  if l:
    lines.append(l)
  else:
    break

for l in lines:
  print l
