'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
'''

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
  
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
  
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # final result
        res = 0
        # temp count 
        count = 0
        # start index
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                k -= 1
                count = 0
            while k == 0:
                count += 1
                k += nums[i] % 2
                i += 1
            res += count
        return res      


