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

# DFS classical problem
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            # up, left, down, right
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!= "1":
                return
            grid[i][j] = "#"
            # up, left, down, right
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)
            dfs(grid,i+1,j)
            dfs(grid,i,j+1)
                
        cnt = 0 
        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # cnt cannot put outside of if, otherwise it will count 0 case as well
                if grid[i][j] == "1":
                    dfs(grid,i,j)
                    cnt += 1
        return cnt
    
