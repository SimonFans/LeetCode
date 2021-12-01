class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # 采用延迟策略做决定。不在开始就决定哪一步用砖块，哪一步用梯子
        # 最理想情况就是高度差大的时候用梯子，小的时候用砖块
        heap = []
        for i in range(len(heights) - 1):
            height_diff = heights[i+1] - heights[i]
            # next building height is lower than the current building
            if height_diff < 0:
                continue
            heapq.heappush(heap, height_diff)
            # 当梯子数量不够用的时候，找出之前高度差最小的尝试用砖块解决
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            # 砖块都用完了，就停留在此
            if bricks < 0:
                return i
        return len(heights) - 1
