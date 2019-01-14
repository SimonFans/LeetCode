A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # row:m, column:n
        
        count=[[0 for t in range(n)] for x in range(m)]
        count[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    count[i][j]=1
                elif i==0:
                    count[i][j]=count[i][j-1]
                elif j==0:
                    count[i][j]=count[i-1][j]
                else:
                    count[i][j]=count[i-1][j]+count[i][j-1]
        return count[m-1][n-1]
