class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        ## LCS 2D DP + Reconstruct SCS

        m = len(str1)
        n = len(str2)

        # dp[i][j] 表示：str1[i:] 和 str2[j:] 的 LCS 长度
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 先计算 LCS
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if str1[i] == str2[j]:
                    # 当前字符可以共享
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                else:
                    # 当前字符不同，
                    # 尝试跳过 str1[i] 或 str2[j]
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )


        # 根据 LCS table 构造 shortest common supersequence
        i = 0
        j = 0
        result = []

        while i < m and j < n:

            if str1[i] == str2[j]:
                # 两边当前字符相同，只需要放一次，然后两边一起前进
                result.append(str1[i])
                i += 1
                j += 1

            elif dp[i + 1][j] >= dp[i][j + 1]:
                # 跳过 str1[i] 仍能保留更长的 LCS，所以先把 str1[i] 放进结果
                result.append(str1[i])
                i += 1

            else:
                # 否则先放 str2[j]
                result.append(str2[j])
                j += 1

        # 如果 str1 还有剩余字符，全部加入
        while i < m:
            result.append(str1[i])
            i += 1

        # 如果 str2 还有剩余字符，全部加入
        while j < n:
            result.append(str2[j])
            j += 1

        return ''.join(result)


        ## Time: O(mn)
        ## Space: O(mn)


        