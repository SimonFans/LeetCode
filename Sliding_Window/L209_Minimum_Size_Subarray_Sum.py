'''
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
'''

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
  
Input: target = 4, nums = [1,4,4]
Output: 1

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
  
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: The subarray [4,3] has the minimal length under the problem constraint.
        
        Input: target = 4, nums = [1,4,4]
        Output: 1
        
        Input: target = 11, nums = [1,1,1,1,1,1,1,1]
        Output: 0
        '''
        # The length of the List
        n = len(nums)
        minLen = float('Inf')
        left, right = 0, 0 
        _sum = 0
        while right < n:
            _sum += nums[right]
            while _sum >= target:
                minLen = min(minLen, right-left+1)
                _sum -= nums[left]
                left += 1
            right += 1
        return 0 if minLen == float('Inf') else minLen
      
