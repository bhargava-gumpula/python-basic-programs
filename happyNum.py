def split_num(num):
    num_list = []
    while num > 0:
        remainder = num % 10
        num_list.insert(0,remainder)
        num = num // 10
    return num_list

def square_digits_sum(num):
    sum = 0
    while num > 0:
        remainder = num % 10
        sum = sum + remainder**2
        num = num//10
    return sum


def happyNumCheck(num):
        #165
        while num >= 10:
            num = square_digits_sum(num)
        if num == 1:
            return True
        else:
            return False


number = int(input("Enter A Number To Check If It Is Happy : "))
happy_num = happyNumCheck(number)
print(happy_num)
