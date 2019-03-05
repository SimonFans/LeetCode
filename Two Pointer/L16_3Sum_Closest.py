Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums)<3:
            return 0
        Min=nums[0]+nums[1]+nums[2]
        for k in range(0,len(nums)-2):
            left=k
            mid,right=k+1,len(nums)-1
            while mid<right:
                tmp=target-nums[left]-nums[mid]-nums[right]
                if abs(tmp) < abs(target-Min):
                    Min=nums[left]+nums[mid]+nums[right]
                if nums[left]+nums[mid]+nums[right]==target:
                    return Min
                elif nums[left]+nums[mid]+nums[right]<target:
                    mid+=1
                else:
                    right-=1
        return Min
