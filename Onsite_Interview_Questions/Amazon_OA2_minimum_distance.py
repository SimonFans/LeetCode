# question default rows=3,columns=3, 9 is the target, so you will get 3 as result because (0,0)->(1,0)->(2,0)->(2,1) three times
"""
1   0   0
1   0   0
1   9   1
"""

class solution():
    def minimumDistance(self,area):
        nRows=len(area)
        nColumns=len(area[0])
        if len(area)==0 or len(area[0])==0 or len(area)!=nRows or len(area[0])!=nColumns:
            return -1
        queue=[]
        # set this point has been visited
        area[0][0]=0
        queue.append((0,0))
        # set direction
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        dist=0
        while queue:
            size=len(queue)
            while size>0:
                size-=1
                cur=queue.pop(0)
                for dir in direction:
                    row=cur[0]+dir[0]
                    column=cur[1]+dir[1]
                    if row>=0 and row<nRows and column>=0 and column<nColumns and area[row][column]!=0:
                        if area[row][column]==9:
                            return dist+1
                        area[row][column]=0
                        queue.append((row,column))
             dist+=1
        return -1


area=[[1,0,0],[1,0,0],[1,9,1]]
print(solution().minimumDistance(area))

