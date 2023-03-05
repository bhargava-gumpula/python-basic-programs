def soloNum(nums):
    x = 0
    while x <= len(nums) // 2 :
        if nums[x] == nums[x+1]:
            if x + 1 < len(nums):
            	del nums[x]
            	del nums[x+1]
            	print(nums)
        x += 1

nums = [1,2,2]
result = soloNum(nums)
print(result)
