Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

题目提示为DP，创建一个新的result list作为memory空间，记录到某个index位置的之前全部数字的sum值。

即，result[0, 1, 2, 3] = result[ nums[0], nums[0] + nums[1],  nums[0] + nums[1] + nums[2], nums[0] + nums[1] + nums[2] + nums[3]]

所以，需要求得sumRange(i, j) 的时候，就是需要result[j] - result[i], 即：result[0, ..., j] - result[0, ..., i] = result[ i+1, ... ,j], 
但是因为包含i, j。所以,需要加上index = i位置的值。最终就是result[j] - result[i] + nums[i]

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.result = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.result.append(sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.result[j]-self.result[i]+self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


