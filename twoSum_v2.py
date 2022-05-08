list = []
while True:
  choice = input("What item do you want in your list (if not type no): ")
  if choice == "no":
      break
  list.append(int(choice))
target = input("What is the target number : ")
target = int(target)
list.sort()
i = 0
j = len(list) - 1
while i != j:
    if list[i] + list[j] == target:
        print (list[i], ",", list[j])
        break
    if list[i] + list[j] > target:
        j -= 1
    if list[i] + list[j] < target:
        i += 1
