class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        ## 2D Bottom-up DP
        
        m = len(s)
        n = len(t)

        # dp[i][j] 表示：用 s[i:] 匹配 t[j:] 的方案数量
        #
        # 多开一行和一列，
        # 用来表示某个字符串已经遍历完的 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 如果 t 已经全部匹配完，
        # 不管 s 还剩多少字符，都有 1 种方法：后面的 s 全部不选
        for i in range(m + 1):
            dp[i][n] = 1

        # 从后往前计算，因为 dp[i][j] 依赖下一行的状态
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if s[i] == t[j]:
                    # 选择 1：使用 s[i] 匹配 t[j]
                    use = dp[i + 1][j + 1]

                    # 选择 2：跳过当前 s[i]
                    skip = dp[i + 1][j]

                    # 两种选择对应不同方案，所以相加
                    dp[i][j] = use + skip

                else:
                    # 当前字符不同，s[i] 不能用于匹配
                    # 只能跳过 s[i]
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]


        ## Time: O(mn)
            # DP table 有：(m + 1) × (n + 1)个状态。
            # 每个状态只做常数级操作：比较字符、加法、赋值
            # 所以：Time = O(mn)

        ## Space: O(mn)
            # DP table：dp = O(mn)
            # 其他变量：O(1)
            # 所以：Space = O(mn)