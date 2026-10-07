class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] = 前 i 个字符的 decode 方法数
        dp = [0] * (n + 1)

        dp[0] = 1  # empty prefix = one valid way
        # 第一个字符不能是 0
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, n + 1):
            # 最后一位单独 decode
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            # 最后两位一起 decode
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

# Time: O(n)
# Space: O(n)