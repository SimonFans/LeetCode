Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 加一个变量记录访问到哪行，然后基数反过来，偶数正常放入list
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        res=[]
        if root==None:
            return res
        queue.append(root)
        l=0
        
        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if l%2==1:
                res.append(level[::-1])
            else:
                res.append(level)
            l+=1
        return res
        
        
