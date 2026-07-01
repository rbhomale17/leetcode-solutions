class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1 and grid[-1][-1] == 1:
            return 0

        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    queue.append((i, j, 0))
                else:
                    grid[i][j] = -1

        while queue:
            r, c, dist = queue.pop(0)

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == -1:
                        grid[nr][nc] = dist + 1
                        queue.append((nr, nc, dist + 1))

        def check(limit):
            if grid[0][0] < limit:
                return False

            queue = [(0, 0)]
            visited = set()
            visited.add((0, 0))

            while queue:
                r, c = queue.pop(0)

                if r == m - 1 and c == n - 1:
                    return True

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] >= limit:
                        if (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))

            return False

        l = 0
        r = 2 * n - 2
        ans = 0

        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans


# class Solution:

#     # Directions for moving to neighboring cells: right, left, down, up
#     dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#     def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
#         n = len(grid)

#         multi_source_queue = deque()
#         # Mark thieves as 0 and empty cells as -1, and push thieves to the queue
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     # Push thief coordinates to the queue
#                     multi_source_queue.append((i, j))
#                     # Mark thief cell with 0
#                     grid[i][j] = 0
#                 else:
#                     # Mark empty cell with -1
#                     grid[i][j] = -1

#         # Calculate safeness factor for each cell using BFS
#         while multi_source_queue:
#             size = len(multi_source_queue)
#             while size > 0:
#                 curr = multi_source_queue.popleft()
#                 # Check neighboring cells
#                 for d in self.dir:
#                     di, dj = curr[0] + d[0], curr[1] + d[1]
#                     val = grid[curr[0]][curr[1]]
#                     # Check if the cell is valid and unvisited
#                     if self.isValidCell(grid, di, dj) and grid[di][dj] == -1:
#                         # Update safeness factor and push to the queue
#                         grid[di][dj] = val + 1
#                         multi_source_queue.append((di, dj))
#                 size -= 1

#         # Binary search for maximum safeness factor
#         start, end, res = 0, 0, -1
#         for i in range(n):
#             for j in range(n):
#                 # Set end as the maximum safeness factor possible
#                 end = max(end, grid[i][j])

#         while start <= end:
#             mid = start + (end - start) // 2
#             if self.isValidSafeness(grid, mid):
#                 # Store valid safeness and search for larger ones
#                 res = mid
#                 start = mid + 1
#             else:
#                 end = mid - 1

#         return res

#     # Check if a given cell lies within the grid
#     def isValidCell(self, grid, i, j) -> bool:
#         n = len(grid)
#         return 0 <= i < n and 0 <= j < n

#     # Check if a path exists with given minimum safeness value
#     def isValidSafeness(self, grid, min_safeness) -> bool:
#         n = len(grid)

#         # Check if the source and destination cells satisfy minimum safeness
#         if grid[0][0] < min_safeness or grid[n - 1][n - 1] < min_safeness:
#             return False

#         traversal_queue = deque([(0, 0)])
#         visited = [[False] * n for _ in range(n)]
#         visited[0][0] = True

#         # Breadth-first search to find a valid path
#         while traversal_queue:
#             curr = traversal_queue.popleft()
#             if curr[0] == n - 1 and curr[1] == n - 1:
#                 return True  # Valid path found

#             # Check neighboring cells
#             for d in self.dir:
#                 di, dj = curr[0] + d[0], curr[1] + d[1]
#                 # Check if the neighboring cell is valid and unvisited
#                 if self.isValidCell(grid, di, dj) and not visited[di][dj] and grid[di][dj] >= min_safeness:
#                     visited[di][dj] = True
#                     traversal_queue.append((di, dj))

#         return False  # No valid path found


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna