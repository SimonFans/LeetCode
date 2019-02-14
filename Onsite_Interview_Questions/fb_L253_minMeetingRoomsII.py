Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

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
