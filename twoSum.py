end = False
list = [1,2,4,7]
print("The list of numbers is 1, 2, 4, and 7")
target = int(input("Choose and number from 1 - 10 : "))

for x in list:
        for i in list:
                if x + i == target:
                        end = True
                        print(x,i)
                        break

                else:
                        continue
        if end == True:
                break
if end == False:
        print("There were no numbers matching the target")

startNum = 0
endNum = 3
end = False
while True:
        if list[startNum] + list[endNum]== target:
                print(list[startNum], list[endNum])
		end = True
                break
        elif list[startNum] + list[endNum] > target:
                endNum = endNum - 1
                continue
        elif list[startNum] + list[endNum] < target:
                startNum = startNum + 1
                continue
if end == False:
	print("There were no numbers matching the target')
