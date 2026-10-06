class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # 先把所有 treasure 加入 queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Multi-source BFS
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # 越界 or 不是未访问的 land
                if (nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    grid[nr][nc] != 2147483647):
                    continue

                # 当前格子的距离 + 1
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))

# Time: O(m * n)
# Space: O(m * n)