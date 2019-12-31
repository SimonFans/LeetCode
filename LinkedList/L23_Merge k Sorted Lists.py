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

class solution(object):
    def mergeKList(self,lists):
        if len(lists)==0:
            return None
        while len(lists)>1:
            nextLists=[]
            for i in range(0,len(lists)-1,2):
                nextLists.append(self.merge(lists[i],lists[i+1]))
            if len(lists)%2==1:
                nextLists.append(lists[len(lists)-1])
            lists=nextLists
        return lists[0]

    def merge(self,l1,l2):
        len1 = len(l1)
        len2 = len(l2)

        i=0
        j=0
        res=[]
        if len1==0:
            return l2
        if len2==0:
            return l1

        while i<len1 and j<len2:
            if l1[i]<l2[j]:
                res.append(l1[i])
                i+=1
            else:
                res.append(l2[j])
                j+=1
        
        while i<len(l1):
            res.append(l1[i])
            i+=1
        while j<len(l2):
            res.append(l2[j])
            j+=1

        return res

array=[[1,3,5],[2,9],[6,8,10]]
test=solution()
print(test.mergeKList(array))

#Result:
[1, 2, 3, 5, 6, 8, 9, 10]

