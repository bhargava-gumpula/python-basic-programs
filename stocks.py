stocks = [3, 4, 2, 5, 3, 8, 6, 1]
biggest = 0
smallest = 0
for x in range(0, len(stocks)):
    if stocks[x] > stocks[biggest]:
        biggest = x
    
for y in range(0, biggest):    
    if stocks[y] < stocks[smallest]:
        smallest = y

print("Buy at %s" % stocks[smallest])
print("Sell at %s" % stocks[biggest])
