def dupRemove(array):
	for x in array:
		for i in array:
			if x == i:
				continue
			if array[x] == array[i]:
				del array[x]
			


user_array = input("Enter your Array of Numbers : ")
user_array = user_array.split(",")
user_array = [eval(i) for i in user_array]

result = dupRemove(user_array)
print(result)
