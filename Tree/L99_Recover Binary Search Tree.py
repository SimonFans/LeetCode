Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return
            else:
                dfs(root.left)
                node_val.append(root)
                dfs(root.right)
        
        node_val = []      
        dfs(root)
        # Because BST is sorted after implemeting inorder traversal, this question just has 2 nodes problem
        first, second = None, None
        for i in range(len(node_val)-1):
            if node_val[i].val >= node_val[i+1].val and not first:
                first = node_val[i]
            # has found first
            if node_val[i].val >= node_val[i+1].val and first:
                second = node_val[i+1]
        
        first.val, second.val = second.val, first.val
        
        
        
