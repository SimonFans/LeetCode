Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:return []
        res = [[1]]
        for i in range(1,numRows):
            res.append(list(map(lambda x,y:x+y,res[-1]+[0],[0]+res[-1])))
        return res
