# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        # if key value < root.val, then search left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # if key value > root.val, then search right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # find to be deleted node
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            '''
            if to be deleted node has left and right node
            then take the minimum value from right subtree
            then use this recursion to delete the minimum value from right subtree
            '''
            tmp = root.right
            mini = tmp.val
            while tmp.left:
                tmp = tmp.left
                mini = tmp.val
            root.val = mini
            root.right = self.deleteNode(root.right, mini)
        return root
      
      
