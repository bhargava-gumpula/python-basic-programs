
def maxOf2Nums(one, two):
	global hello
	hello = "hello1234"
	if one > two:
		return one
	else:
		return two	

# main()

num1 = input("Enter your first number : ")
num2 = input("Enter your second number : ")


max = maxOf2Nums(num1, num2)
print(max)

print(hello)
