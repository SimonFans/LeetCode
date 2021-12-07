Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

 
Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Add root to the stack
        stack = [root]
        
        # dictionary to keep track of parent node
        parent = {root: None}
        
        # loop stops until we found out p & q
        while p not in parent or q not in parent:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        
        # create a set to keep the ancestor of node p
        ancestors = set()
        
        # process all ancestors for node p using parent pointers
        while p:
            ancestors.add(p)
            p = parent[p]
            
        while q not in ancestors:
            q = parent[q]
        
        return q
       
# recursive:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # bottom up
        def helper(node):
            if not node:
                return False
            left = helper(node.left)
            right = helper(node.right)
            mid = node == p or node == q
            # return final result
            if mid + left + right >= 2:
                self.ans = node
            return mid or left or right
            
        self.ans = None
        helper(root)
        return self.ans

       
        
