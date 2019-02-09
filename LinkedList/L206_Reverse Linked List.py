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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur=head
        pre=None
        while cur:
            nextNode=cur.next
            cur.next=pre
            pre=cur
            cur=nextNode
        return pre
        
        
  # Recursive:
  
  class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head,None)

    def _reverse(self, node, prev):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
        
        