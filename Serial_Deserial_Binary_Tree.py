from collections import deque

class Node:
    def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

class solution:
    """Encodes a tree to a single string.
    """
    def serialize(self,root):

        if not root:
            return ""
        q=deque([root])

        res=[]
        while q:
            cur=q.popleft()
            if cur:
                res.append(str(cur.data))
                q.append(cur.left)
                q.append(cur.right)
            else:
                res.append("#")
        return ",".join(res)

    def deserialize(self,data):
        """Decodes your encoded data to tree"""
        if not data:
            return None
        q=deque()
        root=cur=None
        is_left=True
        for s in data.split(","):
            t=None
            if s!="#":
                t=Node(int(s))
                q.append(t)
            if root:
                if is_left:
                    cur.left=t
                else:
                    cur.right=t
                    if not q: return root
                    cur=q.popleft()
                is_left=not is_left
            else:
                if not q: return root
                root=cur=q.popleft()
            return root

root=Node(1)
root.left=Node(2)
root.right=Node(3)

test=solution()
print(test.serialize(root))
print(test.deserialize(test.serialize(root)))
