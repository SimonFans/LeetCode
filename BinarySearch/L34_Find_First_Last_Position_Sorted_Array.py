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
        def searchBound(nums, target, flag):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    # flag=True means find the first position
                    if flag:
                        # mid == left => 已经在最左边了
                        # nums[mid-1] < target => 当前即为 first position
                        if mid == left or nums[mid-1] < target:
                            return mid
                        # search on the left side 
                        else:
                            right = mid - 1
                    # flag=False means find the last position
                    else:
                        # mid == right => 已经在最右边了
                        # nums[mid-1] > target => 当前即为 last position
                        if right == mid or nums[mid+1] > target:
                            return mid
                        # search on the right side 
                        else:
                            left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
                            
        lower_bound = searchBound(nums, target, flag = True)
        if lower_bound == -1:
            return [-1, -1]
        upper_bound = searchBound(nums, target, flag = False)
        return [lower_bound, upper_bound]
    
    

