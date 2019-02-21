Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    self.dfs(grid,r,c)
                    res+=1
        return res
    
    def dfs(self,grid,i,j):
        dirs=[[-1,0],[0,1],[1,0],[0,-1]]
        grid[i][j]="0"
        for d in dirs:
            nc,nr=i+d[0],j+d[1]
            if nc>=0 and nr>=0 and nc<len(grid) and nr<len(grid[0]):
                if grid[nc][nr]=="1":
                    self.dfs(grid,nc,nr)
