# Find the largest continous numbers

class Solution:
    def getMaxIncrement(self, nums):
        anchor = 0
        pos = []
        ans = 0
        # edge case
        if len(nums)== 1:
            return [1]
        # loop from the second number to the end of the array
        for i in range(1, len(nums)):
            # if the next number is not increment by 1, then update the anchor
            if nums[i-1] + 1 != nums[i]: 
                anchor = i
            # if the next number is incremented by 1, then save (anchor, max_reach_position), update the max_reach_position
            else:
                if i - anchor + 1 > ans:
                    pos = []
                    pos.append((anchor, i - anchor + 1))
                ans = max(ans, i - anchor + 1)
        
        return [nums[left:left + length] for left, length in pos]

nums = [1,2,3,4,1,2,3,4,5,1,2,3,4,5]
nums1 = [1,2,3,-1,0,1]
nums2 = [1,2,1,2,1,2]
nums3 = [1]
nums4 = []
Solution().getMaxIncrement(nums3)
