Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_index = 0
        count = 1
        for i in range(1,len(nums)): 
            if nums[maj_index] == nums[i]: 
                count += 1
            else: 
                count -= 1
            if count == 0: 
                maj_index = i 
                count = 1
        return nums[maj_index] 
        
     
