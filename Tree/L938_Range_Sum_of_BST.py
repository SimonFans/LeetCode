Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.


Method 1: Iterative BFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans=0
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                if L<=node.val<=R:
                    ans+=node.val
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans


Method 2: Inorder traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.temp=[]
        res=0
        self.helper(root,L,R)
        
        left=self.temp.index(L)
        right=self.temp.index(R)
        for i in range(left,right+1):
            res+=self.temp[i]
        return res
        
    def helper(self,root,L,R):
            
        if root is None:
            return 
        
        self.helper(root.left,L,R)
        self.temp.append(root.val)
        self.helper(root.right,L,R)
        
        
        
        
      
      
