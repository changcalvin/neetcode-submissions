class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        ## 直接 DP 求 SCS 长度 + Reconstruct

        m = len(str1)
        n = len(str2)

        # dp[i][j] 表示：str1[i:]和str2[j:]的shortest common supersequence长度
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 如果 str2 已经走完，只能把 str1 剩余字符全部加入
        for i in range(m + 1):
            dp[i][n] = m - i
        # 如果 str1 已经走完，只能把 str2 剩余字符全部加入
        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if str1[i] == str2[j]:
                    # 当前字符相同，只需要放一次
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                else:
                    # 当前字符不同，可以先放 str1[i] 或先放 str2[j]
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )


        # 根据 dp table 恢复一个最短答案
        i = 0
        j = 0
        result = []

        while i < m and j < n:

            if str1[i] == str2[j]:
                # 公共字符只放一次
                result.append(str1[i])
                i += 1
                j += 1

            elif dp[i + 1][j] <= dp[i][j + 1]:
                # 先放 str1[i] 能得到不更长的 SCS
                result.append(str1[i])
                i += 1

            else:
                # 先放 str2[j]
                result.append(str2[j])
                j += 1

        # 加入剩余字符
        result.extend(str1[i:])
        result.extend(str2[j:])

        return ''.join(result)

        # Time = O(mn)
        # Space = O(mn)
        