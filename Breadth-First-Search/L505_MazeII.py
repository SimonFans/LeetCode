'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).
'''


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: 12
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # row, col of maze
        row, col = len(maze), len(maze[0])
        # use heapq to extract the (x,y) with the minimum distance 
        heap = []
        # 将起始点加入堆 => (距离，x, y)
        heapq.heappush(heap, (0, start[0], start[1]))
        # 记录走到当前位置的最小距离
        visited = {(start[0], start[1]): 0}
        
        # 循环直到内部到达目的地，返回距离值
        while heap:
            dist, x, y = heapq.heappop(heap)
            # if reach to the destination
            if x == destination[0] and y == destination[1]:
                return dist
            # steps into four directions 
            for _x, _y in ((-1,0),(1,0),(0,-1),(0,1)):
                _newX, _newY, step = x, y, 0
                # Not beyond the row, col edge and not the wall
                while 0 <= _newX + _x < row and 0 <= _newY + _y < col and maze[_newX + _x][_newY + _y] != 1:
                    _newX += _x
                    _newY += _y
                    step += 1                                                
                if (_newX, _newY) not in visited or dist + step < visited[(_newX, _newY)]:
                    visited[(_newX, _newY)] = dist + step
                    heapq.heappush(heap, (dist + step, _newX, _newY))
        return -1
      
      
