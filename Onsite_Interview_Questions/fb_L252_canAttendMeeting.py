For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    
    def canAttendMeetings(self, intervals):

        intervals.sort(key = lambda x:(x.start, x.end))
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
