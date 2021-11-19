Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[l]:
                if nums[mid]>target and target>=nums[l]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<nums[r]:
                if nums[mid]<target and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
    
    
    Solution 2:
        class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, start, end, target):
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    return mid
            return -1      
        
        
        front_right = 0
        end_left = 0
        end_right = len(nums) - 1 
        ans = -1
        
        for i in range(end_right,0,-1):
            if nums[i-1] > nums[i]:
                front_right = i - 1
                end_left = i
                break

        if target >= nums[0] and target <= nums[front_right]:
            ans = binary_search(nums, 0, front_right, target)
        elif target >= nums[end_left] and target <= nums[end_right]:
            ans = binary_search(nums, end_left, end_right, target)
        return -1 if ans == -1 else ans
    
