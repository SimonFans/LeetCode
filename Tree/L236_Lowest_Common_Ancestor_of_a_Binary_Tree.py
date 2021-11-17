# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root : None}
        
        while p not in parent or q not in parent:
            current_node = stack.pop(0)
            if current_node.left:
                stack.append(current_node.left)
                parent[current_node.left] = current_node
            if  current_node.right:
                stack.append(current_node.right)
                parent[current_node.right] = current_node
        
        ancestor = set()
        # loop ends until p is None, which means till reaches to the root
        # why ancestor add before parent is p could be the root node otherwise we will miss that
        while p:
            ancestor.add(p)
            p = parent[p]
        
        while q not in ancestor:
            q = parent[q]
        return q
        
        
        
#         def helper(current_node):
#             # If reach to the end of branch, return False
#             if not current_node:
#                 return False
            
#             # Left recursion
#             left = helper(current_node.left)
            
#             # Right recursion
#             right = helper(current_node.right)
            
#             # if current node is one of p or q
#             mid = current_node == p or current_node == q
            
#             # If any one two of the three flags become True
#             if mid + left + right > 1:
#                 self.ans = current_node
#                 # return self.ans
            
#             # Return True if either of the three bool values is True
#             return mid or left or right
            
#         self.ans = None
#         helper(root)
#         return self.ans
        
