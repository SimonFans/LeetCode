Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        注意这里是一个二叉搜索树，根结点的右子树上所有的点的值都比根结点大，左子树上所有点的值都比根结点的值小
        分为四种情况，
        1、如果两个节点一个值比节点大，一个小，那么二者的公共节点肯定是根结点，
        2、如果两个节点中有一个与根结点的值同样大，那么二者的公共节点同样是根结点
        3、如果两个节点的值都比根结点小，那么二者的公共节点出现在根结点的左子树中，递归查询
        4、如果两个节点的值都比根结点大，那么二者的公共节点出现在根结点的右子树中，递归查询

        """
        if (p.val-root.val)*(q.val-root.val)<=0:
            return root
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
