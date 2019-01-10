 Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cmax=maxSum=nums[0]
        for i in range(1,len(nums)):
            cmax=max(nums[i],nums[i]+cmax)
            maxSum=max(cmax,maxSum)
        return maxSum
        
        
 思路：    
 # maxSum指针记录此前所有碰到的最大值，curSum指针记录循环到当前元素这一轮的最大值。
 当循环到元素i时，如果i+curSum < i的话，说明此前的和是负的，需要舍弃，所以将curSum的值变为i，
 反之，将curSum的值变为i+curSum，表明当前的和还是正值,每一次遍历一个元素之后都会比较一下curSum和maxSum
