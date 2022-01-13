You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return TreeNode(val)
            if node.val > val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            return node
        return dfs(root)
