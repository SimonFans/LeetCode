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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        heap = []
        def inOrderTraversal(node, target):
            if not node:
                return
            inOrderTraversal(node.left, target)
            heapq.heappush(heap, (abs(node.val-target), node.val))
            inOrderTraversal(node.right, target)
        inOrderTraversal(root, target)
        return heap[0][1]
        
        
