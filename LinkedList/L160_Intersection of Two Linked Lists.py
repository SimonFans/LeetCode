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
        def length(p):
            n=0
            while p:
                n+=1
                p=p.next
            return n
        
        if headA is None or headB is None:
            return None
        
        tmp1=headA
        tmp2=headB
        n1=length(tmp1)
        n2=length(tmp2)

        while n1>n2:
            tmp1=tmp1.next
            n1-=1
        
        while n1<n2:
            tmp2=tmp2.next
            n2-=1
            
        while tmp1 != None:
            if tmp1==tmp2:
                return tmp1
            tmp1=tmp1.next
            tmp2=tmp2.next
        return None
    

