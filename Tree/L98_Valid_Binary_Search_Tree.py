Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

            
Method 1: idea: return false if root value is smaller than min(left side tree), if root value is greater than max(right side tree)
    
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root,float('-inf'),float('inf'))
        
    def valid(self,root,min,max):
        if not root:
            return True
        
        if root.val>=max or root.val<=min:
            return False
        
        return self.valid(root.left,min,root.val) and self.valid(root.right,root.val,max)
    
Method 2: Inorder Traversal then for loop compare if the first one is smaller than the second one             
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res=[]
        self.inOrder(root,res)
        for i in range(len(res)-1):
        #考虑到如果根节点和它的左节点或者右节点相等的情况，中序后光大于不行
            if res[i]>=res[i+1]:
                return False
        return True
            
        
    def inOrder(self,root,res):
        if root is None:
            return 
        self.inOrder(root.left,res)
        res.append(root.val)
        self.inOrder(root.right,res)
        
        
