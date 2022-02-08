Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        Solution: Binary Search
                  Index map to matrix: row = mid//n,  column = mid %n
        '''
        m, n  = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1
        while left <= right:
            mid = left + (right - left)//2
            if target < matrix[mid//n][mid%n]:
                right = mid - 1
            elif target > matrix[mid//n][mid%n]:
                left = mid + 1
            else:
                return True
        return False
      

