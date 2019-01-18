Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1 对集合进行排序 2，进行剪枝，如果元素重复，直接跳过这一元素
       
       
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        nums.sort()
        res = []
        previousNum=None
        for i in range(len(nums)):
            # i前面的数和i后面的数
            if nums[i]==previousNum: continue
            previousNum=nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res
