class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ## 2D Bottom-up DP

        m = len(text1)
        n = len(text2)

        # dp[i][j] 表示：
        # text1[i:] 和 text2[j:] 的最长公共子序列长度
        #
        # 多开一行和一列（m和n），表示其中一个字符串已经遍历完
        # i = 0, 1, ..., m
        # j = 0, 1, ..., n
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 因为 dp[i][j] 依赖右边、下边和右下角，
        # 所以从右下往左上计算
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if text1[i] == text2[j]:
                    # 当前字符相同：
                    # 可以把这个字符加入 LCS，
                    # 然后两个字符串都往后移动
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                else:
                    # 当前字符不同：
                    # 尝试跳过 text1[i] 或跳过 text2[j]
                    # 取两种选择中的较大值
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )

        return dp[0][0]


        ## Time: O(mn)
            # DP table 一共有：(m + 1) × (n + 1)个状态。
            # 每个状态只做常数级比较和 max：O(1)
            # 所以：Time = O(mn)

        ## Space: O(mn)
            # dp table：O(mn)
            # 其他变量：O(1)
            # 所以：Space = O(mn)