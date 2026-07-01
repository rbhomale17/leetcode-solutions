class Solution:
    def trapRainWater(self, heightMap):
        def rec(i, j, i1, j1):
            tot = 0
            pending.remove((i1, j1))
            counted.add((i1, j1))
            tot += heightMap[i][j] - heightMap[i1][j1]
            if (i1 - 1, j1) in pending:
                tot += rec(i, j, i1 - 1, j1)
            if (i1, j1 + 1) in pending:
                tot += rec(i, j, i1, j1 + 1)
            if (i1 + 1, j1) in pending:
                tot += rec(i, j, i1 + 1, j1)
            if (i1, j1 - 1) in pending:
                tot += rec(i, j, i1, j1 - 1)
            return tot
        m, n = len(heightMap), len(heightMap[0])
        pending, counted = set(), set()
        tot = 0
        pts = sorted([(i, j) for i in range(m) for j in range(n)], key=lambda a: heightMap[a[0]][a[1]])
        for i, j in pts:
            pending.add((i, j))
            if i == 0 or i == m - 1 or j == 0 or j == n - 1 or \
                (i - 1, j) in counted or \
                (i, j + 1) in counted or \
                (i + 1, j) in counted or \
                (i, j - 1) in counted:
                stk = [(i, j)]
                tot += rec(i, j, i, j)
        return tot

