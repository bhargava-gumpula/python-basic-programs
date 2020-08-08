
snum = 1
user_num = input("Enter a number:")
evens = 0
odds = 0
while snum <= user_num:
    if snum % 2 == 0:
        evens = evens + 1
    else:
        odds = odds + 1
    snum = snum + 1
print ("There are %d even numbers") % (evens)
print ("There are %d odd numbers") % (odds)
