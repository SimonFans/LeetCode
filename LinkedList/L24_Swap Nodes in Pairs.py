Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

思路：
'''
        -1             1  ->   2  ->  3  ->  4
        dummy         head
        prev_node
        
        -1             2  ->   1  ->  3  ->  4
        dummy                        head
                            prev_node
        
        order: -1 & 2 link,  1 & 2 after link, 2 & 1 link
'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # because question said the node value is > 0 so I can use 0 as my dummy node
        dummy = ListNode(0)
        
        # Link to the head
        dummy.next = head
        
        # Set another pointer points to the dummy node
        pre_node = dummy
        
        # Iterate through the Linkedlist
        while head and head.next:
            first_node = head
            second_node = head.next
            
            # swap the first and second
            pre_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            
            # update pre_node and head
            pre_node = first_node
            head = first_node.next
            
        return dummy.next
