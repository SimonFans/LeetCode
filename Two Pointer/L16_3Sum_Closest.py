Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('Inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i+1, len(nums) - 1
            while lo < hi:
                _sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - _sum) < abs(diff):
                    diff = target - _sum
                if _sum < target:
                    lo += 1
                else:
                    hi -= 1
            # optimize 
            if diff == 0:
                break
        return target - diff
        
