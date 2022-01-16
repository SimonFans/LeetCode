'''
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

'''

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
   
Input: n = 1
Output: 1
  
class Solution:
    def countArrangement(self, n: int) -> int:
        # backtracking recursion
        def helper(lst, index):
            # when list is empty, which means the current permutation is valid so return 1 to add into the count
            if len(lst) == 0:
                return 1
            ans = 0 
            for i in range(len(lst)):
                if lst[i]%index == 0 or index%lst[i] == 0:
                    ans += helper(lst[:i] + lst[i+1:], index + 1)
            return ans
        
        # create a list to include numbers from 1 to n
        lst = [i for i in range(1,n+1)]
        
        return helper(lst, 1)
      
