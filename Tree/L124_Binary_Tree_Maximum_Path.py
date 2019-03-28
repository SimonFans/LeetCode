Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        Solution.max=-10000
        Solution.elements=[]
        Solution.path=[]
        
        if not root:
            return Solution.max
        self.maxSum(root,Solution.elements)
        Solution.elements.sort()
        self.dfs(Solution.elements,Solution.max,0,[])
        print(Solution.path)
        return Solution.max
    
    def maxSum(self, root,u):
        if not root:
            return 0
        u.append(root.val)
        lmax=max(0,self.maxSum(root.left,u))
        rmax=max(0,self.maxSum(root.right,u))
        if lmax+rmax+root.val > Solution.max:
            Solution.max=lmax+rmax+root.val
        return max(lmax,rmax)+root.val
        
    
    def dfs(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in Solution.path: 
            return Solution.path.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], i + 1, valuelist + [candidates[i]])
