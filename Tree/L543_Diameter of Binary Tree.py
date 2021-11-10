'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
  
  
Input: root = [1,2]
Output: 1
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def helper(node):
            nonlocal diameter
            if not node:
                return 0
            left_path = helper(node.left)
            right_path = helper(node.right)
            # [2,4,5] => 2 current max diameter
            diameter = max(diameter, left_path + right_path)
            return 1 + max(left_path, right_path)
        helper(root)
        return diameter
        
        
