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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.max=-10000000
        if root==None:
            return 0
        self.maxSum(root)
        return Solution.max
        
    def maxSum(self,root):
        if root==None:
            return 0
        lmax=max(0,self.maxSum(root.left))
        rmax=max(0,self.maxSum(root.right))
        Solution.max=max(Solution.max,lmax+rmax+root.val)
        return max(lmax,rmax)+root.val
