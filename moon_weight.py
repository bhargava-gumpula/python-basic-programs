def moon_weight(weight):
  return weight * 0.165

def calc_weight(weight, years):
  num = 1
  while num <= years:
    weight = weight + 2.3 
    num = num + 1
  return weight

weight = input("ENTER YOUR WEIGHT")
print ("Current Earth weight: %d, Moon Weight: %d") % (weight, moon_weight(weight))

weight = calc_weight(weight, 15)
print ("after 15 years,Earth weight: %d, Moon Weight: %d") % (weight, moon_weight(weight))

weight = calc_weight(weight, 20)
print ("After 20 years, Earth weight: %d, Moon Weight: %d") % (weight, moon_weight(weight))
