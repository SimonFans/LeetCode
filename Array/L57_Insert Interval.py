Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
  
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
  
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
  
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
  

  class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # get the length of intervals
        idx, n = 0, len(intervals)
        res = []
        
        # Add all intervals that start before new interval start date
        while idx < n and newInterval[0] > intervals[idx][0]:
            res.append(intervals[idx])
            idx += 1
        
        # Add new interval
        # If there's no overlap, just add the new interval
        if not res or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        # If there's an overlap, merge with the last interval
        else:
            res[-1][1] = max(res[-1][1], newInterval[1])
        
        # Add the rest of intervals
        while idx < n:
            if res[-1][1] < intervals[idx][0]:
                res.append(intervals[idx])
            else:
                res[-1][1] = max(res[-1][1], intervals[idx][1])
            idx += 1
        return res
  
