Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numLen, res, dict = len(nums), set(), {}
        if numLen < 4: return []
        nums.sort()
        for p in range(numLen):
            for q in range(p+1, numLen): 
                if nums[p]+nums[q] not in dict:
                    dict[nums[p]+nums[q]] = [(p,q)]
                else:
                    dict[nums[p]+nums[q]].append((p,q))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target-nums[i]-nums[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j: res.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return [list(i) for i in res]
        
        
