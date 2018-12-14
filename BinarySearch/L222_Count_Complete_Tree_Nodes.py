Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        hl=self.leftDepth(root)
        hr=self.rightDepth(root)
        if(hl==hr):
            return (1<<hl)-1
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
        
    def leftDepth(self,root):
        h=0
        while root:
            h+=1
            root=root.left
        return h
        
    def rightDepth(self,root):
        h=0
        while root:
            h+=1
            root=root.right
        return h
