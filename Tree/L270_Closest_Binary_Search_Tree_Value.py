'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Input: root = [1], target = 4.428571
Output: 1

求解找到离target值最近的node value

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        node_lst = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            node_lst.append(node.val)
            inorder(node.right)
            return node_lst
        inorder(root)
        print(node_lst)
        i, j = 0, len(node_lst) - 1
        while i + 1 < j:
            mid = i + (j-i)//2
            if node_lst[mid] == target:
                return node_lst[mid]
            elif node_lst[mid] > target:
                j = mid
            else:
                i = mid
        if abs(node_lst[i]-target) > abs(node_lst[j]-target):
            return node_lst[j]
        else:
            return node_lst[i]
