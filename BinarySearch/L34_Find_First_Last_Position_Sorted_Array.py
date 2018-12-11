Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=self.findLeft(nums,target)
        r=self.findRight(nums,target)
        if l<=r:
            return [l,r]
        else:
            return [-1,-1]
        
        
    def findLeft(self,nums,target):
        l,mid,r=0,0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l
    
    def findRight(self,nums,target):
        l,mid,r=0,0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid-1
        return r


