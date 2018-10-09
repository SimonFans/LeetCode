# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        array=self.inOrder(root)
        print(array)
        if not array:
            return None
        newRoot=TreeNode(array[0])
        curr=newRoot
        for i in range(1,len(array)):
            curr.right=TreeNode(array[i])
            curr=curr.right
        return newRoot
        
    def inOrder(self,root):
        if not root:
            return []
        array=[]
        array.extend(self.inOrder(root.left))
        array.append(root.val)
        array.extend(self.inOrder(root.right))
        return array
