Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
  
  
Input: nums = [0]
Output: [[],[0]]
  
  
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.
        '''
#         def backtrack(first=0, curr=[]):
#             # if the current combination is done  which means length of curr == k 
#             if len(curr) == k:
#                 ans.append(curr[:])
#                 return
#             for i in range(first, n):
#                 curr.append(nums[i])
#                 backtrack(i+1, curr)
#                 print(curr)
#                 curr.pop()
#                 print(curr)
        
#         ans = []
#         n = len(nums)
#         # why n+1 because you want to cover empty case, k => all subsets of length k
#         for k in range(n+1):
#             backtrack()
#         return ans


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
