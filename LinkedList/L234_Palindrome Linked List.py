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

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        # find the center point of the list
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        slow=slow.next
        slow=self.reverseList(slow)
        
        while slow:
            if head.val!=slow.val:
                return False
            slow=slow.next
            head=head.next
        return True
        
    def reverseList(self,head):
        newHead=None
        while head:
            p=head
            head=head.next
            p.next=newHead
            newHead=p
        return newHead
