def numeralConverter(nums):
        result = 0
        romanTable = {"I" : 1,
                      "V" : 5,
                      "X" : 10,
                      "L" : 50,
                      "C" : 100,
		      "D" : 500,
		      "M" : 1000}
        nums = nums.upper()
        nums = list(nums)
        x = 0
        while x < (len(nums) - 1):
                if nums[x] == "I" or nums[x] == "X" or nums[x] == "C":
                        if romanTable[nums[x]] < romanTable[nums[x+1]]:
                            result = result + romanTable[nums[x+1]] - romanTable[nums[x]]
                            
                            
                        else: 
                            result = result + romanTable[nums[x]] + romanTable[nums[x+1]]
                            
                        x += 2
                else:
                        result = result + romanTable[nums[x]]
                        x = x + 1
        if x != len(nums):
	        result = result + romanTable[nums[len(nums)-1]]
        return result

roman = input("Choose a roman numeral : ")
result = numeralConverter(roman)
print(result)
