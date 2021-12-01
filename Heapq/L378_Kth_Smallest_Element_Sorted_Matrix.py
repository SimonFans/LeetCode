class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        matrix = [ [1,5,9],
                   [10,11,13],
                   [12,13,15] ]
        k = 8
        Return 13
        '''
        # Get # of rows
        N = len(matrix)
        
        # min_heap
        mini_heap = []
        
        # If k < N, only need to check k row. If k > N, check N row and keep pop and push to find the result
        # ((col#, row#, 当前行第几个元素))
        for r in range(min(k,N)):
            heapq.heappush(mini_heap, (matrix[r][0], r, 0))
        
        while k:
            element, r, c = heapq.heappop(mini_heap)
            if c < N-1:
                heapq.heappush(mini_heap, (matrix[r][c+1], r, c+1))
            k -= 1
        return element
