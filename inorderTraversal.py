class Node:
    def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data


class solution1:

    def inorderTraversal(self,root):
        ans=[]
        self.dfs(root,ans)
        return ans


    def dfs(self,root,ans):
        if not root: return
        self.dfs(root.left, ans)
        ans.append(root.data)
        self.dfs(root.right, ans)

class solution2:
    def inorderTraversal(self,root):
        if not root: return []
        ans,q=[],[]
        self.allLeftStack(root,q)
        while q:
            t=q.pop()
            ans.append(t.data)
            if t.right:
                self.allLeftStack(t.right,q)
        return ans


    def allLeftStack(self,root,q):
        while root:
            q.append(root)
            root=root.left

root=Node(1)
root.right=Node(2)
root.right.left=Node(3)
test=solution1()
test2=solution2()
print(test.inorderTraversal(root))
print(test2.inorderTraversal(root))
