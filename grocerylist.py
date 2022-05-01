shop_items = ["tomato", "potato", "bread", "soup", "pizza", "cucumber", "candy", "juice", "eggs", "milk", "ice cream", "cabbage", "carrots"]
prices = [1.50, 0.33, 2.5 , 3.5, 8.0, 0.45, 0.6, 3.5, 2.5, 2.85, 6.0, 0.8, 0.9]
grocery_list = ["soup", "pizza", "candy", "juice"]
total_cost = 0

for search_item in grocery_list:
    for item in shop_items:
        if item == search_item:
            item_index = shop_items.index(item)
            item_price = prices[item_index]
            total_cost = total_cost + item_price
            break
print "the total cost is : ",  total_cost

