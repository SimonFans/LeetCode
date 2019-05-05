Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res=[]
        self.helper(root,sum,res,[root.val])
        return res
    
    def helper(self,root,target,res,path):
        if not root:
            return
        if sum(path)==target and not root.left and not root.right:
            res.append(path)
            return
        if root.left:
            self.helper(root.left,target,res,path+[root.left.val])
        if root.right:
            self.helper(root.right,target,res,path+[root.right.val])
            
            
