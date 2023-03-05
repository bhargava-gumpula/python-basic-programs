def squareRoot(num):
        x = 0
        oddNum = 1
        while num > 0:
                num = num - oddNum
                oddNum += 2
                x = x+1
	
        if num == 0:
            return x
        if num < 0:
            x = x-1
            return x

# main() entry point
num = int(input("What number do you want to square root : "))
sqrt = squareRoot(num)
print(sqrt)
