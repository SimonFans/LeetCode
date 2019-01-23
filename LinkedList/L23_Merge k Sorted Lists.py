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
        
        
#### Method2 divide and conquer nlogn

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        while len(lists)>1:
            nextLists = []
            for i in range(0,len(lists)-1,2):
                nextLists.append(self.mergeLists(lists[i],lists[i+1]))
            if len(lists)%2==1:
                nextLists.append(lists[len(lists)-1])
            lists = nextLists
        return lists[0]
        
    def mergeLists(self, list1, list2):
        dummy = ListNode(0)
        list = dummy
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                list.next = list1
                list1 = list1.next
            else:
                list.next = list2
                list2 = list2.next
            list = list.next
        if list1 == None:
            list.next = list2
        else:
            list.next = list1
        return dummy.next
