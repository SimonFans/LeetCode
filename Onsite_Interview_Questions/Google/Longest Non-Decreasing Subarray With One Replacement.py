Tags: Array, Dynamic Programming, Two Pointers  
Difficulty: Medium

Given an integer array nums, find the maximum length of a contiguous non-decreasing subarray if you may change at most one element to any value.

A subarray is non-decreasing if:

nums[i] <= nums[i + 1]

for every adjacent pair inside the subarray.

Return the maximum possible length.

Example

Input:

    nums = [1, 0, 3, 4, 5, 2, 3]

Output:

    5

Explanation:

Change nums[1] from 0 to 1.

The array becomes:

    [1, 1, 3, 4, 5, 2, 3]

Then:

    [1, 1, 3, 4, 5]

is a non-decreasing contiguous subarray of length 5.

Therefore, the answer is 5.





from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        left = [1] * n
        right = [1] * n
        
        # 1. 计算以每个位置结尾的最长不减子数组长度
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                left[i] = left[i - 1] + 1
                
        # 2. 计算以每个位置开始的最长不减子数组长度
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1
                
        # 初始化答案为不修改任何元素时的最大长度
        ans = max(left)
        
        # 3. 尝试通过修改第 i 个元素来桥接左右两端
        for i in range(n):
            a = left[i - 1] if i - 1 >= 0 else 0
            b = right[i + 1] if i + 1 < n else 0
            
            if i - 1 >= 0 and i + 1 < n and nums[i - 1] > nums[i + 1]:
                # 无法直接桥接，取单边最大值 + 1
                ans = max(ans, a + 1, b + 1)
            else:
                # 可以完美桥接，合并两端 + 1
                ans = max(ans, a + b + 1)
                
        return ans

# 示例测试
sol = Solution()
nums = [1, 0, 3, 4, 5, 2, 3]
print(sol.longestSubarray(nums))  # 输出: 5
