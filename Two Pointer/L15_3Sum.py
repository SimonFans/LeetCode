Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

### as for list, 
## nums.sort() is faster than sorted(nums) because sorted() will create a new copy. nums.sort() will sort itself, no need to assign
## to a new variable.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i == 0 or nums[i-1] != nums[i]:
                j, k = i+1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        k -= 1
        return list(res)
        return list(res)
                
                    
