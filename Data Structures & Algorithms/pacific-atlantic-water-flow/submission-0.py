class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    (nr, nc) in visited or
                    heights[nr][nc] < heights[r][c]):
                    continue
                dfs(nr, nc, visited)

        # top / bottom
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)

        # left / right
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)

        # 同时可以到达两个 ocean
        return [[r, c] for r, c in pac if (r, c) in atl]