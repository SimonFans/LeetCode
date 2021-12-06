Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            index = idx_map[val]
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)
            return root
        
        idx_map = {node_val : idx for idx, node_val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
        
        
