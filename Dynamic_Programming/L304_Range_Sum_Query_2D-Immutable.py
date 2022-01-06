'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
'''

Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Matrix:
[3, 0, 1, 4, 2] 

[5, 6, 3, 2, 1] 

[1, 2, 0, 1, 5] 

[4, 1, 0, 1, 7] 

[1, 0, 3, 0, 5] 

dp:
  
[[0, 0, 0, 0, 0, 0],
 [0, 3, 3, 4, 8, 10],
 [0, 8, 14, 18, 24, 27],
 [0, 9, 17, 21, 28, 36],
 [0, 13, 22, 26, 34, 49],
 [0, 14, 23, 30, 38, 58]]



class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        # 外层(left, up)加一层0
        self.dp = [[0 for _ in range(num_cols+1)] for _ in range(num_rows+1)]
        # 画图x存的是从坐上走到当前的和 x = C+ B - [0] + x
        # C: (0,0) -> (2,1)的和
        # B: (0,0) -> (1,2)的和
        # [0]: (0,0)
        # x: matrix矩阵中对应的值
        '''
         0 | 0  | 0
        ------------
         0 | A  | B      
        ------------
         0 | C  | x
        '''
        for i in range(1,num_rows+1):
            for j in range(1,num_cols+1):
                self.dp[i][j] = self.dp[i][j-1] + self.dp[i-1][j] - self.dp[i-1][j-1] + matrix[i-1][j-1]
         
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 如果想计算ABCD region, D - *0R - *0L + L0
        # *0L: (0,0) -> (2,0)的和记录在*0L
        # *0R: (0,0) -> (0,2)的和记录在*0R
        # D: 当前矩阵总和
        # L0: 多减了一次需要补上
        '''
        L0 | 0 |*0R
        -----------
        0  | A | B      
        -----------
        *0L| C | D
        '''
        if not self.dp:
            return 0
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
