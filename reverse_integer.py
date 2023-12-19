num = int(input("Enter any number : "))

new_num =  ""
num1 = str(num).split("-")
if len(num1) == 2:
        for x in str(num1[1]):
                new_num = x + new_num
        print("-"+ str(int(new_num)))

else:
        for x in str(num1[0]):
                new_num = x + new_num
        print(int(new_num))

