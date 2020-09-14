string = raw_input("ENTER EXPRESSION:")
num_1 = ""
num_2 = ""
operator = None
for char in string:
    if char  == '+' or char == '-' or char == '*' or char == '/':
       operator = char
       continue
    if operator == None:   
       num_1 += char
    else:
       num_2 += char

num_1 = int(num_1)
num_2 = int(num_2)

if operator == '+':
    value = num_1 + num_2
elif operator == '-':
    value = num_1 - num_2
elif operator == '*':
    value = num_1 * num_2
elif operator == '/':
    value = num_1 / num_2     
print ("%d %c %d = %d") % (num_1, operator, num_2, value)                   
