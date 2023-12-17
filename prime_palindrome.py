def reverse_str(string):
	str1 = ""
	for x in str(string):
		str1 = x + str1
	return str1 
		
def palindrome(num):
	reversed_str = reverse_str(str(num))
	if str(num) == reversed_str:
		return True
	else:
		return False
	
def prime(num):
	prime = True
	for y in range(2, num // 2 + 1):
		if num % y == 0:
			prime = False
			break
	return prime

start = input("Enter your start number : ")
end = input("Enter your end number : ")		
for x in range(int(start), int(end) + 1):
	if prime(x) == True and palindrome(x) == True:
		print(str(x))


