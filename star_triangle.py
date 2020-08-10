def star(num):
   star = "*"
   space = ' '
   num2 = num - 1
   for x in range(1, num * 2, 2):
        print (space * num2) + (star * x)
        num2 = num2- 1
num = input("ENTER AND NUMBER:")
star(num)
