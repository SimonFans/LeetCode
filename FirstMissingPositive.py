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

"""
while:
1. nums[i]>0 => only consider positive number
2. nums[i]< len(nums) => if larger than len(nums), value cannot fall into the list
3. nums[nums[i]-1]!=nums[i] => 判断是不是当前这个值的index对应的是这个值，不是则交换
return n+1: when nums=[] <empty>
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                temp=nums[nums[i]-1]
                nums[nums[i]-1]=nums[i]
                nums[i]=temp
        for j in range(n):
            if nums[j]!=j+1:
                return j+1
        return n+1

A=[3,4,-1,1]
test=solution()
print(test.First_Missing_Positive(A))
