class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        
        def bfs(row, col, curr_count):
            min_distance = float('Inf')
            queue = deque()
            queue.append([row, col, 0])
            while queue:
                curr_row, curr_col, curr_step = queue.popleft()
                for d in direction:
                    next_row = curr_row + d[0]
                    next_col = curr_col + d[1]

                    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == -curr_count:
                        # update distance matrix
                        total_sum[next_row][next_col] += curr_step + 1
                        # get the shortest distance
                        min_distance = min(total_sum[next_row][next_col], min_distance)
                        # mark the cell that has been visited
                        grid[next_row][next_col] -= 1
                        # add current cell's neighbor into the queue
                        queue.append([next_row, next_col, curr_step + 1])
            return min_distance
                        

        # number of rows in the grid
        rows = len(grid)
        # number of cols in the grid
        cols = len(grid[0])
        # 4 directions 
        direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        # Matrix: save the distance rows* cols
        total_sum = [[0] * cols for _ in range(rows)]
        
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_distance = bfs(row, col, count)
                    count += 1
                    if min_distance == float('Inf'):
                        return -1
        return min_distance
