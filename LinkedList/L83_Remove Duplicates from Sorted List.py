# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        curr=head
        while curr and curr.next:
            tmp=curr.next
            if curr.val!=tmp.val:
                curr=tmp
                tmp=tmp.next
            else:
                curr.next=tmp.next
        return head
