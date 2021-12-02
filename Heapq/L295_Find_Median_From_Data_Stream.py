class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # 刚开始都加入到small里
        if len(self.small) == 0: 
            heapq.heappush(self.small, -num)
            return
        # 如果num大于small里最大的数,则将num加到large里去
        if num > -self.small[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        # num in the large heap比small的多两个，所以要balance
        if len(self.small) - len(self.large) == -2:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        
        # num in the small heap比large的多两个，所以要balance
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return  1.0* (self.large[0] - self.small[0])/2
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
