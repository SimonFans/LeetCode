Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
             

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res=0
        self.helper(root)
        return self.res
    
    def helper(self,root):
        # Use Tree PostOrder Traversal
        if root:
            lres,lcount,lmin,lmax=self.helper(root.left)
            rres,rcount,rmin,rmax=self.helper(root.right)
            if lres and rres and lmax<root.val<rmin:
                self.res=max(self.res,lcount+rcount+1)
                return True,lcount+rcount+1,min(lmin,root.val),max(rmax,root.val)
            else:
                return False,0,float("inf"),float("-inf")
        
        # float("inf"),float("-inf")的作用是当root.left,root.right为空时，让第一个叶节点满足BST条件，即root节点要大于左边最大节点，小于右边最小节点   
        else:
            return True, 0,float("inf"),float("-inf")
            
            
