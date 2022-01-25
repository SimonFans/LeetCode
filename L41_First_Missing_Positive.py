"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Test cases:

[0,1, 2, 3]
[3,4,-1,1]
[1,-1,3,4]
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # For any negative numbers, turn them to be 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        # 
        for i in range(len(nums)):
            # in case you assigned negative values through the following conditions, the idea is find out the index current number should land in 
            val = abs(nums[i])
            # if num is not inbound, no need to process
            if 1 <= val <= len(nums):
                # if the index that the number should place is > 0, then that position value * -1
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                # if the index that the number should place is == 0, then that position value = - (len(nums)+1)
                elif nums[val-1]  == 0:
                    nums[val-1] = - (len(nums) + 1)
        # iterate loop, if index value is >=0 then means i+1 is the first missing positive            
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums) + 1
    
