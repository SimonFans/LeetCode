Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]


from copy import deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        (1) 如果一个活着的部落，其周围少于2个部落，这个部落会死
        (2) 如果一个活着的部落，其周围部落数在2或者3，这个部落活到下一个迭代中
        (3) 如果一个活着的部落，其周围多于3个部落，这个部落会死
        (4) 如果一个死了的部落，其周围正好等于3个部落，这个部落会活
        """
        if board and board[0]:
            M,N=len(board),len(board[0])
            board_next=deepcopy(board)
            for m in range(M):
                for n in range(N):
                    res=self.LiveOrDead(board,m,n)
                    if res==2:
                        board_next[m][n]=0
                    elif res==1:
                        board_next[m][n]=1
            for m in range(M):
                for n in range(N):
                    board[m][n]=board_next[m][n]
                    
        
    # return 0-nothing,1-live,2-dead 
    
    def LiveOrDead(self,board,i,j):
        step=[(1, 1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
        M,N=len(board),len(board[0])
        countLive=0
        for k in step:
            r,c = i+k[0],j+k[1]
            if 0<=r<M and 0<=c<N:
                if board[r][c]==1:
                    countLive+=1
        # case (1) and (3)
        if countLive<2 or countLive>3:
            return 2
        # case (2) and (4)
        elif board[i][j]==1 or (board[i][j]==0 and countLive==3):
            return 1
        else:
            return 0
            
            
