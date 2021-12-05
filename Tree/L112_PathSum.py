Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # recursive
        if not root:
            return False
        targetSum -= root.val
        # if current node is a leaf node, then check if current sum == 0? 
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
        # iterative
        if not root:
            return False
        q = [(root, targetSum - root.val)]
        while q:
            current_node, remain = q.pop(0)
            if not current_node.left and not current_node.right and remain == 0:
                return True
            if current_node.left:
                q.append((current_node.left, remain - current_node.left.val))
            if current_node.right:
                q.append((current_node.right, remain - current_node.right.val))
        return False

