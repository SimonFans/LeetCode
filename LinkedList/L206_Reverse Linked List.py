Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        pre=None
        
        while head:
            nex=head.next
            head.next=pre
            pre=head
            head=nex
        
        return pre
        
        
# Recursive:
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Recursion base condition
        # head is null only for case input is null
        def helper(head):
            if head == None or head.next == None:
                return head
            reversed_head = helper(head.next)
            head.next.next = head
            head.next = None
            return reversed_head
        return helper(head)
    
    
    
