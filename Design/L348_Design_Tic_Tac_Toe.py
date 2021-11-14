class TicTacToe:

    def __init__(self, n: int):
        # player 1: 1
        # player 2: -1
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        # Know who is the current player
        current_player =  1 if player == 1 else -1
        self.rows[row] += current_player
        self.cols[col] += current_player
        # diagonal (top left to bottom right)
        if row == col:
            self.diagonal += current_player
        # anti_diagonal (bottom left to top right)
        if col == len(self.cols) - row - 1:
            self.antidiagonal += current_player
        # determine if it wins and return the current_player
        n = len(self.cols)
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(self.antidiagonal) == n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
