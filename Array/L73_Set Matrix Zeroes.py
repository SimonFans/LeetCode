Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R=set()
        C=set()
        i=len(matrix)
        j=len(matrix[0])
        for r in range(i):
            for c in range(j):
                if matrix[r][c]==0:
                    R.add(r)
                    C.add(c)
        for r in range(i):
            for c in range(j):
                if r in R or c in C:
                    matrix[r][c]=0
        
        
        
