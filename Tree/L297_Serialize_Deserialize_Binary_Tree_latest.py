##### DFS解法:

# serialize: tree -> string 
# example:   
'''
          1
       2     3
           4   5
'''
# =>
'''
After serialization, you will get string like 1,2,null,null,3,4,null,null,5,null,null,null
'''

# deserialize: string -> tree
# example: based on the above string result, turn it back to tree structure



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # top down method (传参数供后面使用) (dfs preorder)
        def helper_serialize(node, string):
            if node is None:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = helper_serialize(node.left, string)
                string = helper_serialize(node.right, string)
            return string
        return helper_serialize(root, '')
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper_deserialize(lst):
            if lst[0] == 'None':
                lst.pop(0)
                return None
            val = lst.pop(0)
            root = TreeNode(int(val))
            root.left = helper_deserialize(lst)
            root.right = helper_deserialize(lst)
            return root
        
        data_list = data.split(',')
        root = helper_deserialize(data_list)
        return root
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# BFS 解法

# serialize: tree -> string 
# example:   
'''
          1
       2     3
           4   5
'''
# =>
'''
After serialization, you will get string like '1,2,3,#,#,4,5,#,#,#,#'
'''

# deserialize: string -> tree
# example: based on the above string result, turn it back to tree structure

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
            res.append(str(node.val) if node else '#')
        return ','.join(res)    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = [root]
        index = 1
        while q:
            node = q.pop(0)
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root


