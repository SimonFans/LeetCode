Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

# Time complexity O(n)
# reverseList() 方法只是反转链表的一种方法，空间复杂度 O(1). 不借助多余的空间实现反转单链表后半部分，则可以实现空间复杂度 O(1) 的要求

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return True
        
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # odd length only, even length no need, because slow is in the right position
        if fast:
            slow=slow.next
        
        slow=self.reverse_list(slow)
        
        while slow:
            if head.val!=slow.val:
                return False
            head=head.next
            slow=slow.next
        
        return True
    
    def reverse_list(self, slow):
        pre=None
        while slow:
            next_node=slow.next
            slow.next=pre
            pre=slow
            slow=next_node
        return pre
