Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# only python no python3 since it uses heapq library

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
       # from heapq import heappush, heappop, heapify
        heap = []
        for node in lists:
            if node: 
                heap.append((node.val, node))
        #list to heap
        heapq.heapify(heap)
        dummy=ListNode(0)
        cur=dummy
        while heap:
            pop=heapq.heappop(heap)
            cur.next=ListNode(pop[0])
            cur=cur.next
            if pop[1].next:
                heapq.heappush(heap,(pop[1].next.val,pop[1].next))
        return dummy.next
        
        
