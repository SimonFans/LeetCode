# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if head is null
        if not head:
            return head
        
        # get the length of linkedlist
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        # if k > length and k < length
        k = k % length
        if k == 0:
            return head
        
        cur = head
        for _ in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = tail.next
        tail.next = head
    
        return newHead
