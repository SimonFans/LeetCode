Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        # 一行行来 BFS
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        for node in queue:
            if not node:
                continue
            queue += [node.left, node.right]

        return ','.join(
            map(lambda item: str(item.val) if item else '#', queue))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
    
        parts = data.split(',')
        root = self.buildNode(parts[0])
        queue, i = collections.deque([root]), 1

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = map(
                    self.buildNode, (parts[i], parts[i + 1]))
                queue.append(node.left)
                queue.append(node.right)
                i += 2
        return root
        
        
    def buildNode(self, val):
        return None if val == '#' else TreeNode(int(val))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
