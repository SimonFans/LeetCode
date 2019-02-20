Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        if root is None: 
            return 0 
      
        # Base Case : Leaf node.This acoounts for height = 1 
        if root.left is None and root.right is None: 
            return 1
      
        # If left subtree is Null, recur for right subtree 
        if root.left is None: 
            return self.minDepth(root.right)+1
      
        # If right subtree is Null , recur for left subtree 
        if root.right is None: 
            return self.minDepth(root.left) +1 
      
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
        
 
