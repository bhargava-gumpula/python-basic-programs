item_prices = {
               "MACBOOK"    : 2000,
               "IPHONE"     : 1000,
               "APPLEWATCH" : 500,
               }
item = raw_input ("write a device (macbook, iphone, applewatch:")
item = item.upper()
print "your %s is %d dollars" % (item,item_prices[item])


