Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def fill(x,y):
            if x<0 or x>row-1 or y<0 or y>column-1 or board[x][y]!='O':
                return
            queue.append((x,y))
            board[x][y]='D'
            
        def bfs(x,y):
            if board[x][y]=='O':
                queue.append((x,y))
                fill(x,y)
            while queue:
                cur=queue.pop(0)
                i=cur[0]
                j=cur[1]
                fill(i+1,j) # current pos down
                fill(i-1,j) # current pos up
                fill(i,j-1) # current pos left
                fill(i,j+1) # current pos right
                
        
            
        if len(board)==0: return    
        row=len(board)
        column=len(board[0])
        queue=[]
        for i in range(column):
            bfs(0,i)
            bfs(row-1,i)
        for j in range(1,row-1):
            bfs(j,0)
            bfs(j,column-1)
        # At the end, turn all 'D' to 'O', turn all 'O' to 'X'
        for i in range(row):
            for j in range(column):
                if board[i][j]=='D':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
                    
