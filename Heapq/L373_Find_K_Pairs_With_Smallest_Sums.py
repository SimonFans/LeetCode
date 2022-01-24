'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.


Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]


Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

'''



class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1 = len(nums1)
        l2 = len(nums2)
        if not l1 or not l2: return []
        # result
        res = []
        # (_sum, i,j) where _sum is nums[i] + nums[j], i is l1 index, j is l2 index
        heap = []
        # each number in nums1 do sum with nums2 first number
        for i in range(l1):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))
        '''
        nums1: [1,2]
        nums2: [3]
        不用min则index out of range because when k > nums1 and nums2 匹配数量
        '''
        while len(res) < min(k, l1*l2):
            _sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j +1 < l2:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
        return res
      
      
