'''
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
'''

Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
  
Input: root = [1], target = 0.000000, k = 1
Output: [1]
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        ans = []
        def inOrderTraversal(node, target):
            if not node:
                return
            inOrderTraversal(node.left, target)
            heapq.heappush(heap, (abs(node.val-target), node.val))
            inOrderTraversal(node.right, target)
        inOrderTraversal(root, target)
        while k:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans
