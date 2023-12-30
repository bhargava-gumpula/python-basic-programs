dividend = int(input("Enter your dividend : "))
divisor = int(input("Enter your divisor : "))

def division(dividend, divisor):
    count = 0
    while dividend > 0:
        dividend  = dividend - divisor
        count += 1
    if dividend < 0:
        count = count - 1
    return count
    
print(division(dividend, divisor))

x = int(input("Enter your Multiplicand : "))
y = int(input("Enter your Multiplier : "))

def multiplication(x, y):
    product = 0
    for i in range(0, y):
        product = product + x
    return product


print(multiplication(x,y))
