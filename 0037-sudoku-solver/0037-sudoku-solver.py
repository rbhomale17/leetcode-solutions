class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char != '.':
                    self.rows[r].add(char) 
                    self.cols[c].add(char)
                    
                    box_idx = (r // 3) * 3 + (c // 3)
                    self.boxes[box_idx].add(char)

        self.solver(board, 0, 0)
    
    # Helper function
    def solver(self, board, i, j):
        if i == len(board):
            return True

        if j == len(board)-1:
            li = i+1
            lj = 0
        else:
            li = i
            lj = j+1
        if board[i][j] != '.':
            return self.solver(board, li, lj)
        else:
            box_idx = (i // 3) * 3 + (j // 3)
            for num in map(str, range(1, 10)):
                if self.isNumSafe(num, i, j, box_idx):
                    board[i][j] = num
                    
                    self.rows[i].add(num) 
                    self.cols[j].add(num)
                    
                    self.boxes[box_idx].add(num)

                    if self.solver(board, li,lj):
                        return True
                    board[i][j] = '.'
                    self.rows[i].remove(num) 
                    self.cols[j].remove(num)
                    self.boxes[box_idx].remove(num)
        return False

    def isNumSafe(self, num, row, col, box_idx):
            return (    
                num not in self.rows[row] 
                and num not in self.cols[col] 
                and num not in self.boxes[box_idx]
            )


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna