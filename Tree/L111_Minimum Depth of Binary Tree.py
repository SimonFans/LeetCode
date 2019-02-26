Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is None: 
            return 0 
      
        # Base Case : Leaf node.This acoounts for height = 1 
        if root.left is None and root.right is None: 
            return 1
      
        # If left subtree is Null, recur for right subtree 
        if root.left is None: 
            return self.maxDepth(root.right)+1
      
        # If right subtree is Null , recur for left subtree 
        if root.right is None: 
            return self.maxDepth(root.left) +1 
      
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
 
#### BFS method:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        if root==None:
            return 0
        queue=[]
        queue.append(root)
        depth=1
        # cur level记录当前数组中的数目，即当前层的node数，最后条件必须是0才深度加一
        cur_level=1
        # next level记录下一层加进来几个node
        next_level=0
        while queue:
            node=queue.pop(0)
            cur_level-=1
            if node.left==None and node.right==None:
                return depth
            if node.left!=None:
                queue.append(node.left)
                next_level+=1
            if node.right!=None:
                queue.append(node.right)
                next_level+=1
            if cur_level==0:
                cur_level=next_level
                next_level=0
                depth+=1
        return depth
    
