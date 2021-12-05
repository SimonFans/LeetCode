# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def is_uni(node):
            # base case: if the node has no children, then it's a univalue subtree
            if not node.left and not node.right:
                self.count += 1
                return True
            
            # flag is used for recording the current status 
            is_uni_flag = True
            
            if node.left:
                is_uni_flag = is_uni(node.left) and is_uni_flag and node.val == node.left.val
            
            if node.right:
                is_uni_flag = is_uni(node.right) and is_uni_flag and node.val == node.right.val
            
            self.count += is_uni_flag
            return is_uni_flag
        
        
        # bottom up
        # (1) count + 1 when it's a leaf node (the node has no children)
        # (2) count + 1 when all of the node's children have same value
        if not root:
            return 0
        self.count = 0
        is_uni(root)
        return self.count
        
        
