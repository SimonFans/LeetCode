Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return None
        result=None
        mini_diff=sys.maxsize
        
        while root:
            diff=abs(root.val-target)
            
            if diff<mini_diff:
                result=root.val
                mini_diff=diff
            
            if diff==0:
                break
            
            if target>=root.val:
                root=root.right
            else:
                root=root.left
        return result
        
        
