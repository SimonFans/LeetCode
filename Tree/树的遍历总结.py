广度优先遍历：

def breadth_travel(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print node.elem,
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)
                
深度优先遍历：

（1） 先序：

  def preorder(self, root):
        """递归实现先序遍历"""
        if root == None:
            return
        print root.elem
        self.preorder(root.lchild)
        self.preorder(root.rchild)
        
（2） 中序：

def inorder(self, root):
      """递归实现中序遍历"""
      if root == None:
          return
      self.inorder(root.lchild)
      print root.elem
      self.inorder(root.rchild) 
      
(3) 后序：

def postorder(self, root):
      """递归实现后续遍历"""
      if root == None:
          return
      self.postorder(root.lchild)
      self.postorder(root.rchild)
      print root.elem
