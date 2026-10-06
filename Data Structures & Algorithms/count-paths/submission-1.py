class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                top = dp[r-1][c] 
                left = dp[r][c-1] 
                dp[r][c] = top + left

        return dp[m-1][n-1]
