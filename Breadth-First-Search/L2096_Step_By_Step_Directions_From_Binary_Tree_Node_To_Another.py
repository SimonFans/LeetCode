'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
'''

Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
    
       5
   1      2
3  null 6   4

'''
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
'''

     2
  1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # edge case:
        if not root:
            return ''
        # BFS
        q = collections.deque()
        # initial variable:
        startPath = ''
        destPath = ''
        q.append((root, ''))
        while q:
            node, path = q.popleft()
            if node.val == startValue:
                startPath = path
            elif node.val == destValue:
                destPath = path
            if node.left:
                q.append((node.left, path + 'L'))
            if node.right:
                q.append((node.right, path + 'R'))
        i = 0
        while min(len(startPath), len(destPath)) > i and startPath[i] == destPath[i]:
            i += 1
        # RLR RRR , starts from i => destPath[i:] 
        return (len(startPath) - i) * 'U' + destPath[i:]
      
