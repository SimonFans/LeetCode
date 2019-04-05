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
        res=set() # unique result
        for k in range(len(nums)):
            t=-nums[k]
            i,j=k+1,len(nums)-1
            while i<j:
                if nums[i]+nums[j] == t:
                    res.add((nums[k],nums[i],nums[j])) 
                    i+=1
                    j-=1
                elif nums[i]+nums[j] < t:
                    i+=1
                else:
                    j-=1
        return list(res)
                
                    
