# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if head is null
        if not head or k == 0:
            return head
        
        # get the length of linkedlist
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        # in case k > len(linkedlist)
        k = k % length
        
        # if there's no need to do rotation then return head
        if k == 0:
            return head
        
        cur = head
        for _ in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = tail.next
        tail.next = head
    
        return newHead
