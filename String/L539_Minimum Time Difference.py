Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.

重点是排序后加上首个00 +24， 因为0点也是24点

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mini=6000000
        tp=[]
        for p in timePoints:
            hour=int(p.split(':')[0])
            minutes=int(p.split(':')[1])
            tp.append([hour,minutes])
        tp.sort()
        print(tp)
        tp+=[[tp[0][0]+24,tp[0][1]]]
        print(tp)
        for x in range(len(tp)-1):
            temp=(tp[x+1][0] - tp[x][0]) * 60 + tp[x+1][1] - tp[x][1]
            if temp<mini:
                mini=temp
        return mini
        
        
