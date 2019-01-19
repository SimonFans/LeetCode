class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    def sumOfRightLeaves(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root:
            return 0

        if root.right:
            if not root.right.left and not root.right.right:
                res+=root.right.data
            else:
                res += self.sumOfRightLeaves(root.right)

        res += self.sumOfRightLeaves(root.left)
        return res


# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(8)
root.insert(14)
root.insert(3)

#root.PrintTree()
print(root.sumOfRightLeaves(root))



