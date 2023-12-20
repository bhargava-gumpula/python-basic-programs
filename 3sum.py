list = [1, 2, 3, 4, 5]
print("The list is [1,2,3,4,5]")
target = int(input("Enter your target num : "))

def sum3(list, target):
        exit = False
        for x in range(0, len(list)):
                for y in range(1, len(list)):
                        for z in range(2, len(list)):
                            if list[x] + list[y] + list[z] > target:
                                return None

                            if list[x] + list[y] + list[z] == target:
                                return list[x], list[y], list[z]

                            if list[x] + list[y] + list[z] < target:
                                if z == len(list) - 1:
                                    break
                                else:
                                    z = z + 1

                        if y == len(list) - 2:
                            break
                
                if x == len(list) - 3:
                        return None




        return list[x], list[y], list[i]
print(sum3(list, target))
