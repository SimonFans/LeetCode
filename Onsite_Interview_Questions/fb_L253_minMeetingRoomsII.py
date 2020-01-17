Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

# Method 1: heapq

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        # 按开始时间排序
        intervals.sort(key=lambda x:x[0])
        
        # 建立堆结构
        room=[]
        print(intervals[0][1])
        # 放入第一个时间
        heappush(room,intervals[0][1])
        
        for i in intervals[1:]:
            # 如果之前会议最早的结束时间<当前会议的开始时间，就将当前会议结束时间更新为最新结束时间
            if room[0]<=i[0]:
                heappop(room)
            # （1）最近的会议都在开，只能开新房间 （2）找到并延长之前的会议结束时间
            heappush(room,i[1])
        
        # 最后算有多少个结束时间就是多少个房间
        return len(room)

# Method 2:

class solution:
    def minMeetingRoomsII(self,test):

        starts_sort=sorted(test, key=lambda x: x[0])   # [[0,30],[5,10],[15,20]]
        ends_sort=sorted(test,key=lambda x: x[1])      # [[5,10],[15,20],[0,30]]
        starts=[]
        ends=[]
        for i in range(len(test)):                     # run 0, 1, 2
            starts.append(starts_sort[i][0])           #[0,5,15]
            ends.append(ends_sort[i][1])               #[10,20,30]
        res=0
        end=0
        for i in range(len(test)):
            if starts[i]<ends[end]:
                res+=1
            else:
                end+=1
        return res


test=[[0,30],[5,10],[15,20]]
print(solution().minMeetingRoomsII(test))
