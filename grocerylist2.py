shop_items = ["tomato", "potato", "bread", "soup", "pizza", "cucumber", "candy", "juice", "eggs", "milk", "ice cream", "cabbage", "carrots"]
prices = [1.50, 0.33, 2.5 , 3.5, 8.0, 0.45, 0.6, 3.5, 2.5, 2.85, 6.0, 0.8, 0.9]
grocery_list = ["soup", "potato", "ice cream", "eggs"]
total_cost = 0

for i in range(len(grocery_list)):
    search_item = grocery_list[i]
    for j in range(len(shop_items)):
         if search_item == shop_items[j]:
             item_price = prices[j]
             total_cost = total_cost + item_price
             break
print "the total cost is : ", total_cost
