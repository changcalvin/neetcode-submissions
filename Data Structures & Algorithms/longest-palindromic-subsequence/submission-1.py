class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for L in range(n - 1, -1, -1):
            dp[L][L] = 1
            for R in range(L + 1, n):
                if s[L] == s[R]:
                    dp[L][R] = 2 + dp[L + 1][R - 1]
                else:
                    dp[L][R] = max(dp[L + 1][R], dp[L][R - 1])

        return dp[0][n - 1]