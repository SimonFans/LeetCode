Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.


from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        heap = []
        
        #sort the list based on start time
        intervals.sort(key = lambda x: x[0])
        
        # heap push the first meeting end time
        heapq.heappush(heap, intervals[0][1])
        
        # if next start time >= the minimum end time, then it means there's a meeting completes
        # we can pop the minimum end time
        for interval in intervals[1:]:
            if heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        return len(heap)
    
    
