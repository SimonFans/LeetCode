Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

# 滑动窗口求解
"""
left bar (l)
right bar (r)

 l
[10,5,2,6]
 r
 
prod=1
l, ans = 0,0
< r 遍历nums>
  while 1*10 >=K:
      prod/=num[l]
      l+=1
  ans+=r-l+1 <窗口长度即为当前subarray的个数>
  return ans
  
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        left,ans=0,0
        prod=1
        for right in range(len(nums)):
            prod*=nums[right]
            while prod>=k:
                prod/=nums[left]
                left+=1
            ans+=right-left+1
        return ans


