Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

Solution:

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # imagine two heap list, small right, large left
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        # make large & small length balance, keep large side be positive, small side be negative. 
        # Heap's feature: always keep the minimum value at position 0, others may not in order. 
        if len(self.small)==len(self.large):
            heapq.heappush(self.large,-heapq.heappushpop(self.small,-num))
        else:
            heapq.heappush(self.small,-heapq.heappushpop(self.large,num))
            

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (float(self.large[0])-float(self.small[0]))/2
        else:
            return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
