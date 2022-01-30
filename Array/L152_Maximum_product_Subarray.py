Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
  
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
  
'''
Thoughts:
define min_so_far and max_so_far
min_so_far = min(curr_number, curr_number*min_so_far, curr_number* max_so_far)
max_so_far = min(curr_number, curr_number*min_so_far, curr_number* max_so_far)
result 记录更新 max_so_far

example: nums = [2,3,-2,4]
              2   3   -2   4
curr:         2   3   -2   4
min_sofar:    2   3   -12  -48
max_sofar:    2   6   -2   4

Return result 6
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1,len(nums)):
            curr_num = nums[i]
            # temp_so_far is used to not overwritting the max_so_far, otherwise the min_so_far will use calculaated max_so_far give wrong result
            temp_so_far = max(curr_num, curr_num* max_so_far,curr_num *min_so_far)
            min_so_far = min(curr_num, curr_num* max_so_far,curr_num *min_so_far)
            max_so_far = temp_so_far
            result = max(result, max_so_far)
        return result
      
      
