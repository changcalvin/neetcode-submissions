class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        # dp[r][c]：从 (r,c) 出发的最长递增路径长度
        # 0 表示还没有计算过
        dp = [[0] * cols for _ in range(rows)]
        # 四个方向：上、下、左、右
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # 已经计算过，直接返回
            if dp[r][c] != 0:
                return dp[r][c]
            # Base case：只有当前格子，路径长度至少为 1
            dp[r][c] = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 边界检查 + 必须严格递增
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]):
                    # 当前格子 + 从邻居出发的最长路径
                    dp[r][c] = max(dp[r][c], 1 + dfs(nr, nc))
            return dp[r][c]

        # 可以从任意位置开始，取全局最大值
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))

        return res