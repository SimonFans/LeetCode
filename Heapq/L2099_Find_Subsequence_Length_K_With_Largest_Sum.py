'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''
# subsequence 要保证有序

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not n:
            return []
        
        if n < k:
            return []
        
        heap = []
        res = []
        # subsequence must be in order
        for i in range(k):
            heapq.heappush(heap, (nums[i], i))
        for i in range(k, n):
            min_num = heap[0][0]
            if nums[i] > min_num:
                heapq.heappop(heap)
                heapq.heappush(heap, (nums[i], i))
        # sort for case. [50, -75], k =2
        heap.sort(key = lambda x:x[1])
        return [num for (num, _) in heap]
      
