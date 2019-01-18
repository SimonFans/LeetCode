Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root==None:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        path=[]
        
        if root.left!=None:
            path+=[str(root.val)+'->'+ t for t in self.binaryTreePaths(root.left)]
        if root.right!=None:
            path+=[str(root.val)+'->'+ t for t in self.binaryTreePaths(root.right)]
        return path
        
        
