Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix==[]:
            return []
        up,left=0,0
        right=len(matrix[0])-1
        down=len(matrix)-1
        direction=0  # 0: go right, 1: go down, 2: go left 3: go up
        res=[] # result
        while True:
            if direction==0:  # if go right
                for i in range(left,right+1):
                    res.append(matrix[left][i])
                up+=1
            if direction==1: # if go down
                for i in range(up,down+1):
                    res.append(matrix[i][right])
                right-=1           
            if direction==2: # if go left
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
            if direction==3: # if go up
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left+=1
            if up>down or left >right: return res
            direction=(direction+1)%4  # 4 directions
            
            
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        
        if row == 0 or len(matrix[0]) == 0:
            return []
        
        col = len(matrix[0])
        # first line directly added into the list
        res = matrix[0]
        # matix row is > 1
        if row > 1:
            for i in range(1, row):
                res.append(matrix[i][col-1])
                
            for j in range(col-2, -1, -1):
                res.append(matrix[row-1][j])
            if col > 1:
                for k in range(row-2, 0, -1):
                    res.append(matrix[k][0])
        M = []
        for r in range(1, row-1):
            t = matrix[r][1:-1]
            M.append(t)
        return res + self.spiralOrder(M)
       
       
       
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right.
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1

        return result
