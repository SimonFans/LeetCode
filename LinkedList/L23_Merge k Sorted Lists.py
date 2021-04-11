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


# heap法解题 
from heapq import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        cur=head=ListNode(0)
        heap = []
        count=0
        for sorted_list in lists:
            if sorted_list: 
                count+=1
                heapq.heappush(heap,(sorted_list.val, count, sorted_list))
        
        
        while len(heap)>0:
            _,_,cur.next=heapq.heappop(heap) 
            cur=cur.next
            
            if cur.next is not None:
                count+=1
                heapq.heappush(heap,(cur.next.val,count,cur.next))
            
        return head.next
        
        
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
            # 如果lists长度为奇数，则做完上面的for循环，还要再加上list中的最后一部分
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

      
 ## Kth array：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        num_lists = len(lists)
        interval = 1
        while interval < num_lists:
            for i in range(0, num_lists - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i],lists[i + interval])
            interval *= 2
        return lists[0] if num_lists > 0 else None
        
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

array=[[1,3,5],[2,9],[6,8,10]]
test=solution()
print(test.mergeKList(array))

#Result:
[1, 2, 3, 5, 6, 8, 9, 10]

