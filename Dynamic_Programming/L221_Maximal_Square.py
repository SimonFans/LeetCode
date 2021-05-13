'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Input: matrix = [["0"]]
Output: 0

'''

Solution:
  
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        max_side_len = 0
        # 建立二维数组，在原始二维数组基础上加层外墙
        # 行遍历每一个，比较当前点的左上角，左边和上边,取最小值+1，更新边长，最后求面积
        dp = [[ 0 for j in range(col + 1)] for i in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min( dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
                    max_side_len = max(max_side_len, dp[i][j])
        return max_side_len * max_side_len

      
