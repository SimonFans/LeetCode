Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Input: 3
Output: [1,3,3,1]

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[1]
        for i in range(1,rowIndex+1):
            res=list(map(lambda x,y:x+y,res+[0],[0]+res))
        return res
