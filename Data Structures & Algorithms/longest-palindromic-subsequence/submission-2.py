class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        ## 2D Bottom-up DP

        # dp[i][j]表示：s[i:j+1] 这一段里的最长 palindromic subsequence 长度。
        
        # if s[i] == s[j]: dp[i][j] = 2 + dp[i + 1][j - 1]
        # if s[i] != s[j]: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        # 单个字符本身就是长度为 1 的回文子序列
        for i in range(n):
            dp[i][i] = 1

        # 从右往左枚举左边界，保证 dp[i+1][j] 和 dp[i+1][j-1] 已经算好
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):

                if s[i] == s[j]:
                    # 两端字符相同，可以一起放进回文子序列
                    dp[i][j] = 2 + dp[i + 1][j - 1]

                else:
                    # 两端不同，至少舍弃其中一个
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j - 1]
                    )

        return dp[0][n - 1]

        ## Time: O(n²)

        ## Space: O(n²)
