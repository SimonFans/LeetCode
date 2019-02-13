Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

class solution:
    def minMeetingRoomsII(self,test):

        starts_sort=sorted(test, key=lambda x: x[0])
        ends_sort=sorted(test,key=lambda x: x[1])
        starts=[]
        ends=[]
        for i in range(len(test)):
            starts.append(starts_sort[i][0])
            ends.append(ends_sort[i][1])
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
