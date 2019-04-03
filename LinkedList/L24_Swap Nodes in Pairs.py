Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        point=ListNode(0)
        point.next=head
        head=point
        
        while point.next and point.next.next:
            tmp=point.next.next.next        # 3 <-tmp
            point.next.next.next=point.next  # 2->1
            point.next=point.next.next    # 0 -> 2
            point.next.next.next=tmp      # 1 -> 3
            point=point.next.next         # 1 <- point
        
        return head.next 
