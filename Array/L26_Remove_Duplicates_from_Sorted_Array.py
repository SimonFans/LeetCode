Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

'''
Thoughts:
1. 定义一个初始指针index指向数组中第一个数字
2. 从第二个数字开始遍历整个数组，如果发现当前数字不同于index所指向的数字，则index+1，然后更新当前数字到index所指的位置
3. 最后返回index+1即为有多少个distinct numbers
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index=0         # index: 最后数字标记的位置
        for i in range(1,len(nums)):
            if nums[i]!=nums[index]:
                index+=1
                nums[index]=nums[i]
        return index+1
        
        
