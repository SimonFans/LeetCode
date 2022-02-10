'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # heapq.heapify(heap)
        # for num in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap, num)
        #     else:
        #         if heap[0] < num:
        #             heapq.heappop(heap)
        #             heapq.heappush(heap, num)
        # return heap[-k]
        
        heap = [nums[i] for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]
      
 
