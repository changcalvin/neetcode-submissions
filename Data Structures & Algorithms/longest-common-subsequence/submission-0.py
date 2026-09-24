class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ## 1D Bottom-up DP

        # 可选优化：
        # 让 text2 更短，可以进一步减少空间
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m = len(text1)
        n = len(text2)

        # dp[j] 表示：
        # 当前处理到 text1 某个位置时，和 text2[j:] 的 LCS 长度
        dp = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            # 保存原来的 dp[j + 1]，
            # 也就是二维 DP 中的右下角值
            prev_diagonal = 0

            for j in range(n - 1, -1, -1):
                # 当前 dp[j] 在更新前，
                # 代表二维 DP 中“下一行同一列”的值
                old_dp_j = dp[j]

                if text1[i] == text2[j]:
                    # 对应二维 DP：
                    # 1 + dp[i+1][j+1]
                    dp[j] = 1 + prev_diagonal

                else:
                    # dp[j]：
                    # 更新前是 dp[i+1][j]
                    #
                    # dp[j+1]：
                    # 已经更新成 dp[i][j+1]
                    dp[j] = max(
                        dp[j],
                        dp[j + 1]
                    )

                # 给下一次循环保存“右下角”
                prev_diagonal = old_dp_j

        return dp[0]