Given a binary tree, print it vertically. The following example illustrates vertical order traversal.

          1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9 
               
			  
The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # base case
        if not root: return []
        cols = collections.defaultdict(list)
        q = [(root, 0)]
        while q:
            for node, col in q:
                cols[col].append(node.val)
            new_q = []
            for node, col in q:
                if node.left:
                    new_q.append((node.left, col-1))
                if node.right:
                    new_q.append((node.right, col+1))
            q = new_q
            
        return [cols[c] for c in sorted(cols.keys())]



# My thought to make simplify:

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # base case
        if not root: return []
        cols = collections.defaultdict(list)
        q = [(root, 0)]
        while q:
            node,col=q.pop(0)
            cols[col].append(node.val)
            if node.left:
              q.append((node.left, col-1))
            if node.right:
              q.append((node.right, col+1))
           
        return [cols[c] for c in sorted(cols.keys())]
