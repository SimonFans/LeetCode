Description
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the difference between the sum of the two integers and the target.



Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).


思路
这个套路的题就是先排序。
排完从两边往当中走。
当我们发现sum < target，说明要再大一点会更接近target。那么往右走。
反之当sum > target，说明要再小一点会更接近target。那么往左走。


class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumCloset(self, nums, target):
        # Write your code here
        nums.sort()
        i, j = 0, len(nums) - 1
        diff = sys.maxint
        while i < j:
            if nums[i] + nums[j] < target:
                diff = min(diff, target - nums[i] - nums[j])
                i += 1
            else:
                diff = min(diff, nums[i] + nums[j] - target)
                j -= 1
        
        return diff
