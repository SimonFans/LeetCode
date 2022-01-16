'''
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.
'''


Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
  
Input: root = []
Output: []
  
Input: root = [1]
Output: [1]
  
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 
        def dfs(cur):
            if not cur.left:
                return cur
            newRoot = dfs(cur.left)
            cur.left.left = cur.right
            cur.left.right = cur
            cur.left = None
            cur.right = None
            return newRoot
        
        # edge case : given by example 2
        if not root:
            return None
        return dfs(root)

'''
               1
  cur       2      3
 newRoot 4     5
 
'''

