Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummy=ListNode(0)
        cur=dummy
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=ListNode(l1.val)
                l1=l1.next
                cur=cur.next
            else:
                cur.next=ListNode(l2.val)
                l2=l2.next
                cur=cur.next
        while l1:
            cur.next=ListNode(l1.val)
            l1=l1.next
            cur=cur.next
        while l2:
            cur.next=ListNode(l2.val)
            l2=l2.next
            cur=cur.next
        return dummy.next
