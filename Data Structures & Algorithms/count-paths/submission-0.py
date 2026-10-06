class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0: 
                    continue
                top = dp[r-1][c] if r-1 >= 0 else 0
                left = dp[r][c-1] if c-1 >= 0 else 0
                dp[r][c] = top + left
                
        return dp[m-1][n-1]
