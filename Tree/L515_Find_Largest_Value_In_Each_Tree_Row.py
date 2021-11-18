# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            curr_max = float('-Inf')
            for i in range(len(queue)):
                current_node = queue.pop(0)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.val >= curr_max:
                    curr_max = current_node.val
            res.append(curr_max)
        return res
