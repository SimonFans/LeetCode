Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left=0; right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target: return True
            if nums[left]==nums[mid]==nums[right]: # for duplicated number
                left+=1; right-=1
            elif nums[left]<=nums[mid]: # left part
                if nums[left]<=target<nums[mid]: right=mid-1 # target in left part
                else: left=mid+1
            else:                       # right part exp: 4561234, 1:mid,2:target
                if nums[mid]<=target<nums[left]: left=mid+1
                else:right=mid-1
        return False


Actually, this piece of code run in O(logN) when no duplicates exist and only run in O(N) when duplicates exist
