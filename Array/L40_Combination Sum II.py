Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]


class Solution:
    
    # 和上一道题类似。只不过这道题要求candidate中的每个数只能使用一次。也是使用dfs。
    
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        candidates.sort()
        Solution.res = []
        self.dfs(candidates, target, 0, [])
        return Solution.res
        
    def dfs(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in Solution.res: 
            return Solution.res.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], i + 1, valuelist + [candidates[i]])
