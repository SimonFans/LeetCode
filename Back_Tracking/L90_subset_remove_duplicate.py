Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
  
Input: nums = [0]
Output: [[],[0]]
  
'''
think: 
[] [1] [1,2] [1,2,2] [2], [2,2]
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.
        '''
        def backtrack(start = 0, curr=[]):
            ans.append(curr)
            print(ans, start)
            # i -> 0,1,2
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1, curr + [nums[i]])
        ans = []
        nums.sort()
        backtrack()
        return ans
