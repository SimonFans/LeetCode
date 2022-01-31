'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
'''

Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
  
Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return
            # Due to the given property, the most smallest number is the root
            elif node.val != self.mini_val and node.val < self.second_mini_val:
                self.second_mini_val = node.val
            helper(node.left)
            helper(node.right)
            
            
        
        self.mini_val = root.val
        self.second_mini_val = float('Inf')
        helper(root)
        return self.second_mini_val if self.second_mini_val != float('Inf') else -1
      
      
