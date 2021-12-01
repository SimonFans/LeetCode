class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        mini_cost = 0 
        
        for stick in sticks:
            heapq.heappush(heap, stick)
        while heap:
            first = heapq.heappop(heap)
            if heap:
                second = heapq.heappop(heap)
                mini_current = first + second
                mini_cost += mini_current
                heapq.heappush(heap, mini_current)
        return mini_cost 
