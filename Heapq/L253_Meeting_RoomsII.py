'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
'''

import heapq
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
        # we can pop the minimum end time from the heap
        for interval in intervals[1:]:
            if heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        # Finally we can count how many end time left in the heap, that's the answer
        return len(heap)
