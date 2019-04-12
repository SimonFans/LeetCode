Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

    
# Sliding Window
#Time Complexity: O(N), where NN is the length of nums. We perform one loop through nums.

#Space Complexity: O(1), the space used by anchor and ans
    
    
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        ans = anchor = 0
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
        
        
