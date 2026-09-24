class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # 转成 LCS

        # Longest Palindromic Subsequence
        # = s 和 reverse(s) 的 Longest Common Subsequence

        # 比如：s = "bbbab"
        # reverse = "babbb"
        # 然后求：LCS(s, reverse(s))
        
        rev = s[::-1]
        n = len(s)

        # dp[i][j] 表示：s[i:] 和 rev[j:] 的 LCS 长度
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if s[i] == rev[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )

        return dp[0][0]

        ## Time = O(n²)
        ## Space = O(n²)