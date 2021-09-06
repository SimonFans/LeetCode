Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # final result list
        results = []
        
        def backtrack(remain, comb, start):
            if remain == 0:
                # do a deep copy
                results.append(list(comb))
                return
            elif remain < 0:
                return
            # iterate loop
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain-candidates[i], comb, i)
                comb.pop()
        
        backtrack(target, [], 0)
        return results
