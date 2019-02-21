Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
# pre->2  cur->5  4-3-2, node at 4
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        dummy=pre=ListNode(0)
        dummy.next=head
        # note down previous node and move to current node
        for _ in range(m-1):
            pre=pre.next
        cur=pre.next
        # reverse the defined part 
        new_head=None
        for _ in range(n-m+1):
                p=cur
                cur=cur.next
                p.next=new_head
                new_head=p
        # connect to three parts
        pre.next.next=cur
        pre.next=new_head
        return dummy.next
        
        
