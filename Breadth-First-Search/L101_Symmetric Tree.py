Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

####  BFS iterative method:

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        queue=[]
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            t1=queue.pop(0)
            t2=queue.pop(0)
            if t1==None and t2==None:
                continue
            if t1==None or t2==None:
                return False
            if t1.val!=t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
        
        
### Recursive way     
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.helper(root.left,root.right)
        return True
        
    def helper(self,p,q):
        if p==None and q==None:
            return True
        if p and q and p.val==q.val:
            return self.helper(p.right,q.left) and self.helper(p.left,q.right)
        return False
