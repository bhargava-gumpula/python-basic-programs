def fibonocci(x,y,n):
    sequence = []
    while y < n:
    	sequence.append(x)
    	sequence.append(y)
    	x = x + y
    	y = x + y

    if x < n:
        sequence.append(x)		
    print (sequence)

input1 = input("What is the first number in sequence(usually 0) : ")
input2 = input("What is the second number in sequence(usually 1) : ")
maxnum = input("What is the maximum fibonocci number : ")
fibonocci(int(input1),int(input2),int(maxnum))
