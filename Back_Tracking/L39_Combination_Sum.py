# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.


Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
  
  
Input: candidates = [2], target = 1
Output: []
  

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates = [2,3,6,7], target = 7
        # backtracking
        
        res = []
        
        def backTrack(remain, comb, start):
            if remain == 0:
                # deep copy the comb, the way in python is to do list()
                res.append(list(comb))
                return
            
            elif remain < 0:
                return 
            
            for i in range(start, len(candidates)):
                # add the potential answer
                comb.append(candidates[i])
                # give the current number another chance rather than move on 
                print(remain, '-', candidates[i], '->',comb,i )
                backTrack(remain - candidates[i], comb, i)
                # take the one out which added before but not valid 
                comb.pop()
        
        '''
        target value
        use to add potential answer into this list
        start point 
        '''
        backTrack(target, [], 0)
        return res
      
      
