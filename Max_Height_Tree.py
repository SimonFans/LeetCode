class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class solution:
        def maxDepth(self,root):
            if root is None:
                return 0
            else:
                return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

test=solution()

print(test.maxDepth(root))
