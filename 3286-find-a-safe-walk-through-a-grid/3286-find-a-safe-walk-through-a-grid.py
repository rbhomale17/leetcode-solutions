class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        dp = {}  # (i, j, health) -> bool
        if self.solve(dp, 0, 0, grid, health):
            return True
        return False
        
    def solve(self, dp, i, j, mat, health):
        if i < 0 or j < 0 or i > len(mat) - 1 or j > len(mat[0]) - 1:
            return False
        if mat[i][j] == -1:
            return False

        health -= mat[i][j]  # deduct current cell here only

        if health < 1:
            return False

        if i == len(mat) - 1 and j == len(mat[0]) - 1:
            return True

        if (i, j, health) in dp:  # health included in key
            return dp[(i, j, health)]

        temp = mat[i][j]
        mat[i][j] = -1

        dp[(i, j, health)] = (
                self.solve(dp, i, j + 1, mat, health)
            or  self.solve(dp, i, j - 1, mat, health)
            or  self.solve(dp, i + 1, j, mat, health)
            or  self.solve(dp, i - 1, j, mat, health)
        )

        mat[i][j] = temp
        return dp[(i, j, health)]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna