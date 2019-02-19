Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n=len(nums)
        return n*(n+1)//2-sum(nums)

    
# Method 2:

class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        nums.sort()
        if nums[-1]!=len(nums):
            return len(nums)
        if nums[0]!=0:
            return 0
        for i in range(1,len(nums)):
            expected_number=nums[i-1]+1
            if nums[i]!=expected_number:
                return expected_number
