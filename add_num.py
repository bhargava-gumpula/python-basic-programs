list1 = []
list2 = []

for x in range(0,3):
	list1.insert(0,int(input("Enter number %s : " % x)))

for x in range(0,3):
        list2.insert(0,int(input("Enter number %s : " % x)))


def addList(list1, list2):
        final_list = []
        carry_num1 = 0
        carry_num2 = 0
        y_count = 0
        for x in range(0,len(list1)):
                for y in range(0, len(list2)):
                        y = y + y_count
                        if list1[x] + list2[y] + carry_num2 >= 10:
                                carry_num1 = list1[x]+list2[y] + carry_num2 -10
                                carry_num2 = 1
                                final_list.insert(0,carry_num1) 
                        else:
                                final_list.insert(0,list1[x]+list2[y]+carry_num2)
                                carry_num2 = 0
                        y_count = y_count + 1
                        break
        if carry_num2 > 0:
             final_list.insert(0,carry_num2)                
        return final_list

print(addList(list1, list2))
