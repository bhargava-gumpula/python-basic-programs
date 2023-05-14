
def bodyNum(age,height, weight):
	body_num = age*weight/height
	
	return body_num

age = int(input("Enter your age : "))
weight = int(input("Enter your weight : "))
height = int(input("Enter your Height : "))

body_num = bodyNum(age,height,weight)
print(body_num)


#=====================================================


def split(string):
	split_string = []
	for char in string:
		split_string.append(char)
	return split_string

string = input("Enter a string : ")
split_string = split(string)
print(split_string)



#======================================================



def factorial(num):
	result = 1
	for x in range(1,num):
		result = result * x + result
	return result

num = int(input("Enter a number : "))
print(factorial(num))
