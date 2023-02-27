for prime in range(2, 101):
    exit = False
    for i in range(2,prime//2+1):
                if prime % i == 0:
                        exit = True
                        break
    if exit == False:
        print(prime)	
