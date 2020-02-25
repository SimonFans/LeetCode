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
        if not nums:
            return 1

        length = len(nums)
        i = 0
        while i < length:
            if nums[i] <= 0:
                i += 1
            else:
                if nums[i] <= length:
                    if nums[i] == i+1 or nums[nums[i]-1] == nums[i]:
                        # no need to swap
                        i += 1
                        continue
                    tmp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = tmp
                else:
                    i += 1

        i = 0
        while i < length:
            if nums[i] != i + 1:
                return i + 1
            i += 1

        return length + 1  # no missing until length
    
    
A=[3,4,-1,1]
test=solution()
print(test.First_Missing_Positive(A))
