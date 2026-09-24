class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        ## 1D Bottom-up DP

        n = len(t)

        # dp[j] 表示：
        # 用目前处理过的 s，
        # 组成 t[:j] 的方案数量
        dp = [0] * (n + 1)

        # 组成空字符串永远有 1 种方式：
        # 什么都不选
        dp[0] = 1

        for ch in s:
            # 必须倒序更新，
            # 防止同一个 s 字符在同一轮被重复使用
            for j in range(n, 0, -1):
                if ch == t[j - 1]:
                    # 当前字符可以作为 t[j-1]
                    # 所有组成 t[:j-1] 的方案
                    # 都可以通过加入当前字符变成 t[:j]
                    dp[j] += dp[j - 1]

        return dp[n]

        ## Time = O(mn)
        ## Space = O(n)
        