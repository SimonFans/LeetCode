Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

Example 1:
intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5]

4-1
     -8-4-5
5-0-1

Example 2:
intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4]

0-9-1
     -2-4
3

Example 3: 
return None, there's no intersection.

2-6-4
1-5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         pA = headA
#         pB = headB

#         while pA != pB:
#             pA = headB if pA is None else pA.next
#             pB = headA if pB is None else pB.next
#         return pA
        
        nodes_in_B = set()
        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next
        while headA is not None:
            if headA in nodes_in_B:
                return headA
            headA = headA.next
        return None
    

