"""
[LintCode] 597 Subtree with Maximum Average 解题报告
Description
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.


Example
Given a binary tree:

      1
    /   \
  -5     11
 /  \    /  \
1    2  4   -2

return the node 11.

"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    avg, node = 0, None
    def findSubtree2(self, root):
        if root is None:
            return None
        self.getSubTree(root)
        return self.node
    def getSubTree(self,root):
        if root is None:
            return 0,0
        sumLeft, countLeft = self.getSubTree(root.left)
        sumRight, countRight = self.getSubTree(root.right)
        sumTotal=sumLeft+sumRight+root.val
        countTotal=countLeft+countRight+1
        average=sumTotal*1.0 / countTotal
        if self.node is None or average > self.avg:
            self.node=root
            self.avg=average
        return sumTotal, countTotal
