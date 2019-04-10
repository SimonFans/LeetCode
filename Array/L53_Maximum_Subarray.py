 Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


"""
Initialize:
    max_so_far = -2**31 - 1
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
  
return max_so_far


"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far=-2**31 - 1
        max_end_here=0
        for number in nums:
            max_end_here+=number
            if max_so_far < max_end_here:
                max_so_far=max_end_here
            if max_end_here < 0:
                max_end_here=0
            
        return max_so_far

        
 
