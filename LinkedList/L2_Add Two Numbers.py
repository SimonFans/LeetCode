You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        flag=0
        dummy=ListNode(0)
        p=dummy
        while l1 and l2:
            p.next=ListNode((l1.val+l2.val+flag)%10)
            flag=(l1.val+l2.val+flag)//10
            l1=l1.next
            l2=l2.next
            p=p.next
        while l2:
            p.next=ListNode((l2.val+flag)%10)
            flag=(l2.val+flag)//10
            l2=l2.next
            p=p.next
        while l1:
            p.next=ListNode((l1.val+flag)%10)
            flag=(l1.val+flag)//10
            l1=l1.next
            p=p.next
        if flag==1:
            p.next=ListNode(1)
        return dummy.next
        
        
