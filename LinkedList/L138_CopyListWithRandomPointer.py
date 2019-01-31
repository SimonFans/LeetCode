A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
#   1-2-3-4  1-3, 4-2
# 先复制，字典存储，之后while走random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        pointer,dummy=head,RandomListNode(0)
        newHead=dummy
        nodeDic=dict()
        while pointer:
            newNode=RandomListNode(pointer.label)
            nodeDic[pointer]=newHead.next=newNode
            pointer,newHead=pointer.next,newHead.next
        pointer=head
        newHead=dummy.next
        while newHead:
            if pointer.random:
                newHead.random=nodeDic[pointer.random]
            pointer,newHead=pointer.next,newHead.next
        return dummy.next
