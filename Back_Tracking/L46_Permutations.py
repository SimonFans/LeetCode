Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = []
        for i in range(len(nums)):
            # i前面的数和i后面的数 <[a,b] => a and b switch when only two items left>
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res
