Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


"""
[100, 4, 200, 1, 3, 2]
=>
[1, 2, 3, 4, 100, 200]

"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 判断list是否为空
        if not nums:
            return 0
        # 从小到大排序
        nums.sort()
        # list不为空，所以至少有一个连续值
        curr_streak=1
        max_streak=1
        for i in range(1,len(nums)):
            # [0,1,1,2] 当2个1的时候，跳过第一个1
            if nums[i]!=nums[i-1]:
                if nums[i]==nums[i-1]+1:
                    curr_streak+=1
                else:
                    max_streak=max(max_streak,curr_streak)
                    curr_streak=1
        return max(max_streak,curr_streak)
        
        
