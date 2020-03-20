Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


# Method 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        cur=ListNode(float('-Inf'))
        dummy=cur
        
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        
        cur.next = l1 or l2
        
        return dummy.next

Time complexity : 
O(n+m)

Because exactly one of l1 and l2 is incremented on each loop iteration, 
the while loop runs for a number of iterations equal to the sum of the lengths of the two lists. 
All other work is constant, so the overall complexity is linear.

Space complexity : 
O(1)

The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
    
    
# Method 2 heap sort    
from heapq import *

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        cur=head=ListNode(0)
        heap=[]
        # 增加一个元素在heap里，以防止当值相同的时候对比大小
        count=1
        
        if not l1 and not l2:
            return None
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        heapq.heappush(heap,(l1.val,count,l1))
        count+=1
        heapq.heappush(heap,(l2.val,count,l2))
        
        while len(heap)>0:
            _,_,cur.next=heapq.heappop(heap)
            cur=cur.next
            if cur.next is not None:
                count+=1
                heapq.heappush(heap,(cur.next.val,count,cur.next))
    
        return head.next
