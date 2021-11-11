''''
Given the root of a binary tree, return the leftmost value in the last row of the tree.


Input: root = [2,1,3]
Output: 1

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

'''

# 解题思路： BFS 根节点 -> 右node -> 左node。 层级遍历，取到最后的时候就是最左边的node值

import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS Solution:
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        queue = collections.deque([root])
        ans = None
        while queue:
            size = len(queue)
            for _ in range(size):
                ans = node = queue.popleft()
                if node.right:
                    queue.append(node.right)  
                if node.left:
                    queue.append(node.left)
        return ans.val

# Priority Queue Solution:

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
      if not root:
        return None
      queue = []
      heapq.heappush(queue,(1, 1, root))
      ans = None
      while queue:
        size = len(queue)
        for _ in range(size):
          level, label, node = heapq.heappop(queue)
          ans = node
          if node.right:
            heapq.heappush(queue,(level+1, 2*label + 1, node.right))
          if node.left:
            heapq.heappush(queue,(level+1, 2*label + 2, node.left))
      return ans.val

