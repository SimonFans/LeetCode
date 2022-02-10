'''
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Pre-condition: Each sub list must be sorted
        head = pointer = ListNode(0)
        heap = []
    
        # (list.val, list address)
        '''
        heap:
        [(1, 0, ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}),
         (1, 1, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}), 
         (2, 2, ListNode{val: 2, next: ListNode{val: 6, next: None}})]
        '''
        # list[i] represents the first address of the linkedlist
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))    
    
        while heap:
            cur_val, _, node = heapq.heappop(heap)
            pointer.next = ListNode(cur_val)
            pointer = pointer.next
            node = node.next
            if node:
                i+=1
                heapq.heappush(heap, (node.val, i, node))
        return head.next
      
