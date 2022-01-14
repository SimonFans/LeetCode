'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Input: root = [1], target = 1, k = 3
Output: []

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # BFS Find parents
        parent = {root.val: None} 
        def findParents(root): 
            stack = [root]
            while stack:
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                    parent[node.left.val] = node
                if node.right:
                    stack.append(node.right)
                    parent[node.right.val] = node
            
            # DFS Find parents
            '''
            if not root:
                return
            if root.left:
                parent[root.left.val] = root
                findParents(root.left)
            if root.right:
                parent[root.right.val] = root
                findParents(root.right)
            '''
        
        def bfs(node):
            visited = set() 
            queue = [(node, 0)]
            output = []
            while queue:
                node, dist = queue.pop(0)
                if node and node.val not in visited:
                    visited.add(node.val)
                    if dist == k:
                        output.append(node.val)
                    else:
                        if node.left and node.left not in visited:
                            queue.append((node.left, dist + 1))
                        if node.right and node.right not in visited:
                            queue.append((node.right, dist + 1))
                        if node.val in parent and parent[node.val] not in visited:
                            queue.append((parent[node.val], dist + 1))
            return output
        
        findParents(root)
        return bfs(target)
      
      
