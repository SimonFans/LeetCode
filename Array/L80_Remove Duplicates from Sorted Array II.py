Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums)<=2:
            return len(nums)
        count=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[count-2]:
                nums[count]=nums[i]
                count+=1
        return count
        
        

