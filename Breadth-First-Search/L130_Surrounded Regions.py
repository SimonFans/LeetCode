'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
'''
x x x x
x o o x
x x o x
x o x x
=======
Result:
x x x x
x x x x
x x x x
x o x x
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        思路：把边境扫一遍，有'O'的加入queue做BFS，并且mark一个别的值例如'D'。最后整体扫一遍，再遇到有'O'的，直接mark'X'.遇到'D', mark 'O'
        <1> first for loop check the first row and the last row if there's any 'O'.
            If it is, check if it's out of the range or != 'O', if yes, add to queue do bfs
        <2> second loop is from the second row to the row starts from the last row -1, with col 0 and the last column
        <3> lastly, two for loop through the whole matrix. If meet any values == 'O', mark 'X' means 'O' not at
            the boundary
            If meet any values == 'D', means either 'O' at boundary or 'O' connects to one 'O' at the boundary
        """
        def bfs(x,y):
            if x<0 or x>row-1 or y<0 or y>column-1 or board[x][y]!='O':
                return
            queue.append((x,y))
            board[x][y]='D'
            while queue:
                i, j = queue.popleft()
                bfs(i+1,j) # current pos down
                bfs(i-1,j) # current pos up
                bfs(i,j-1) # current pos left
                bfs(i,j+1) # current pos right

        row=len(board)
        column=len(board[0])
        # BFS
        queue=deque()
        # 最上面的一层，和最下面的一层，从左向右
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
