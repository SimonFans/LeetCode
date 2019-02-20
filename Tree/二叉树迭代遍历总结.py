class TreeIterMixin:
	  def __init__(self, tree):
		  self._root = tree
      self.left=None
      self.right=None
    
    def preorder_traverse(self):
        for x in self._preorder(self._root):
            yield x
    def _preorder(self, node):
        if node:
            yield node
            for x in self._preorder(node.left):
                yield x
            for x in self._preorder(node.right):
                yield x
    def inorder_traverse(self):
        for x in self._inorder(self._root):
            yield x
    def _inorder(self, node):
        if node:
            for x in self._preorder(node.left):
                yield x
            yield node
            for x in self._preorder(node.right):
                yield x
    def postorder_traverse(self):
        for x in self._inorder(self._root):
            yield x
    def _postorder(self, node):
        if node:
            for x in self._preorder(node.left):
                yield x
            for x in self._preorder(node.right):
                yield x
            yield node
    def depth_first_order_traverse(self):
        if self._root:
            stack = Stack()
            stack.push(self._root)
            while not stack.empty():
                node = stack.pop()
                if node.left:
                    stack.push(node.left)
                if node.right:
                    stack.push(node.right)
                yield node
    def breadth_first_order_traverse(self):
        if self._root:
            queue = Queue()
            queue.push(self._root)
            while not queue.empty():
                node = queue.pop()
                if node.left:
                    queue.push(node.left)
                if node.right:
                    queue.push(node.right)
                yield node
