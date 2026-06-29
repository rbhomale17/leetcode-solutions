class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        result = []
        self.nQueens(board, 0, result)
        return result
    
    def nQueens(self, board, row, result):
        if row == len(board):
            result.append(["".join(arr) for arr in board])
            return

        for col in range(len(board)):
            if self.isQueenSafe(board, row, col):
                board[row][col] = "Q"
                self.nQueens(board, row + 1, result)
                board[row][col] = "."

    def isQueenSafe(self, board, row, col):
        # Check row upwords
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # check diagonally upper left
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            
            i -= 1
            j -= 1
        
        
        # check diagonally upper rigth
        k = row - 1
        l = col + 1

        while k >= 0 and l < len(board):
            if board[k][l] == "Q":
                return False
            k -= 1
            l += 1

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna