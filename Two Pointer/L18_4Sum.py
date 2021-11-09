Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        
        for i in range(n):
            for j in range(i+1, n):
                goal = target - nums[i] - nums[j]
                beg, end = j+1, n-1
                while beg < end:
                    if nums[beg] + nums[end] < goal:
                        beg += 1
                    elif nums[beg] + nums[end] > goal:
                        end -= 1
                    else:
                        ans.add((nums[i],nums[j],nums[beg],nums[end]))
                        beg += 1
                        end -= 1
        return ans
        
