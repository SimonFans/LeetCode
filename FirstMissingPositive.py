"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Test cases:

[0,1, 2, 3]
[3,4,-1,1]
[1,-1,3,4]
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 遍历整个list
        for i in range(len(nums)):
            # 第一个条件用于排除负数和大于当前长度的特例，引用当前值的下标值进行判断
            # 第二个条件用于判断是否当前值应该在的位置是否为当前值，如果是则不交换，否则交换。
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        #再次遍历整个list，判断对应位置是否为应当的值，特例是如果没有missing，比如【1，2】则应返回长度+1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
    
    
A=[3,4,-1,1]
test=solution()
print(test.First_Missing_Positive(A))
