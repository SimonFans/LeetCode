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
            
            
