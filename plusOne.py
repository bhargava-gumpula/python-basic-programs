def split_num(num):
    num_list = []
    while num > 0:
        remainder = num % 10
        num_list.insert(0,remainder)
        num = num // 10
    return num_list
        
def plusOne(numbers_list):
    number_string = ""
    for x in numbers_list:
        number_string += str(x)
    number_int = int(number_string)
    number_int += 1
    numbers_list = split_num(number_int)
    return numbers_list
        
bignumber = input("Enter a number seperated by comma's : ")
numbers_list = bignumber.split(",")
number = plusOne(numbers_list)
print(number)
