def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range (len(nums) - 1):
            for j in range (len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return[]

   

def sortedTwoSum(nums, target):
	i = 0
	j = len(nums) - 1
	while True:
		if i > j:
			return []
		if nums[i] + nums[j] < target:	
			i = i+1
		if nums[i] + nums[j] > target:
 			j = j-1		
		if nums[i] + nums[j] == target:
			return [i,j]
		



found = sortedTwoSum([7,2,5,3],1)
if not found:
        print "Coulnd find two sum for target"
else:
       print ("Two Sum indices are %d, %d") % (found[0], found[1])
        
