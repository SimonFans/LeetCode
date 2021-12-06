Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # postorder <-> inorder relationship
        # the order postorder: left, right, root. 
        # can use pop() to get the root then split the inorder list into left subtree and right subtree
        
        def helper(left, right):
            if left > right:
                return None
            
            # pick the last element as root
            val = postorder.pop()
            root = TreeNode(val)
            
            # find index in the inorder based on root value
            index = idx_map[val]
            
            # split the inorder into right subtree
            root.right = helper(index+1, right)
            
            # split the inorder into left subtree
            root.left = helper(left, index-1)
            
            return root
        
        # node_val: idx from inorder
        idx_map = { node_val : idx for idx, node_val in enumerate(inorder)}
        
        return helper(0, len(inorder) - 1)
