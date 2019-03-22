Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

思路： 
stack先压右侧节点，再左侧，之后将新建的node节点右侧指针链接上个节点的左侧，所以要用stack存储
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
      
        stack=[root]
        pointer=TreeNode(None)
        while stack:
            top=stack.pop()
            if not top: continue
            stack.append(top.right)
            stack.append(top.left)
            pointer.right=top
            pointer.left=None
            pointer=top
            
            
