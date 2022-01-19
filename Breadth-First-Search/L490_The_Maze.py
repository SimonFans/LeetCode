'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
    
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false
'''

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # directions
        directions= [(0,-1), (0,1), (1,0), (-1,0)]
        # boundary
        m, n = len(maze), len(maze[0])
        # bfs queue
        queue = deque([(start[0], start[1])])
        # define a seen set to store the visited pos (only store the pos => the last pos when roll to the wall)
        seen = set()
        seen.add((start[0], start[1]))
        
        while queue:
            cur_i, cur_j = queue.popleft()
            for dx, dy in directions:
                ni, nj = cur_i, cur_j
                while 0 <= ni + dx < m and 0 <= nj + dy < n and maze[ni + dx][nj + dy] == 0:
                    ni += dx
                    nj += dy
            # check if current pos is the destination 
                if ni == destination[0] and nj == destination[1]:
                    return True
                if (ni, nj) not in seen:
                    queue.append((ni,nj))
                    seen.add((ni,nj))
        return False
      
      
      
