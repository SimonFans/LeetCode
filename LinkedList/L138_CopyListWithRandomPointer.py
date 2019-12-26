A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

"""
https://www.cnblogs.com/zuoyuan/p/3745126.html

首先，在原链表的每个节点后面都插入一个新节点，新节点的内容和前面的节点一样。比如上图，1后面插入1，2后面插入2，依次类推。

其次，原链表中的random指针如何映射呢？比如上图中，1节点的random指针指向3，4节点的random指针指向2。如果有一个tmp指针指向1（蓝色），则一条语句：tmp.next.random = tmp.random.next；就可以解决这个问题。

第三步，将新的链表从上图这样的链表中拆分出来。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# example: 1-1'-2-2'-3-3'-4-4', random pointer: 1-3, 2-4

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None: return None
        tmp = head
        # (1) duplicate a new node such as: 1-1'-2-2'-3-3'-4-4'
        while tmp:
            newNode = Node(tmp.val)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next
        tmp = head
        # (2) Copy each node random pointer
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        # reset old head and new head (copied one)
        newhead = head.next
        pold = head
        pnew = newhead
        # separate copied one from original one
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        # Return copied one: 1'-2'-3'-4'
        return newhead
    
    
