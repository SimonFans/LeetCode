Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder is None or inorder is None or len(preorder)==0 or len(preorder)!=len(inorder):
            return None
        return self.buildTreeHelper(preorder,inorder,0,0,len(preorder)-1)
        
    def buildTreeHelper(self,preorder,inorder,pre_st,ino_st,ino_end):
        if pre_st>len(preorder) or ino_st>ino_end:
            return None
        current=TreeNode(preorder[pre_st])
        i=ino_st
        while i<=ino_end:
            if inorder[i]==preorder[pre_st]:
                break
            i+=1
        current.left=self.buildTreeHelper(preorder,inorder,pre_st+1,ino_st,i-1)
        current.right=self.buildTreeHelper(preorder,inorder,pre_st+(i-ino_st+1),i+1,ino_end)
        return current
        
        
