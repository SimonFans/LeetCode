Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        
        start,end=0,len(nums)-1
        
        # ensure start & end next to each other at the end
        while start+1<end:
            mid=start+(end-start)//2
            if nums[mid]>=target:
                end=mid
            else:
                start=mid
        if nums[start]>=target:
            return start
        if nums[end]>=target:
            return end 
        return len(nums)
    
    
