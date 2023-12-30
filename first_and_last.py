list = [2, 3, 3, 4, 5, 7, 7, 7, 8, 8, 9]
print("The list is [2,3,3,4,5,7,7,7,8,8,9]")
target = int(input("Enter Your target Number : "))

def first_and_last(list, target):
    location = []
    for x in range(0, len(list)):
        if list[x] == target:
            if list[x + 1] == target:
                if list[x-1] == target:
                    continue
                else:
                    location.append(x)
            else:
                location.append(x)
                
            
    return location

print(first_and_last(list, target))
