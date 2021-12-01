class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        ans = []
        for index, lst in enumerate(mat):
            heap.append((sum(lst), index)) 
        heapq.heapify(heap)
        while k > 0:
            rn = heapq.heappop(heap)
            ans.append(rn[1])
            k -= 1
        return ans
