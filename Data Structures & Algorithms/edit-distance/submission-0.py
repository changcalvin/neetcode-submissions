class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        ## 2D Bottom-up DP
        
        m = len(word1)
        n = len(word2)

        # dp[i][j] 表示：
        # 把 word1[i:] 转换成 word2[j:]
        # 最少需要多少次操作
        #
        # 多开一行和一列，用来处理其中一个字符串已经走完的情况
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 如果 word2 已经走完，
        # word1 剩下的字符都需要删除
        for i in range(m + 1):
            dp[i][n] = m - i

        # 如果 word1 已经走完，
        # word2 剩下的字符都需要插入
        for j in range(n + 1):
            dp[m][j] = n - j

        # 当前状态依赖下、右、右下，
        # 所以从右下往左上计算
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if word1[i] == word2[j]:
                    # 当前字符已经匹配，不需要操作
                    dp[i][j] = dp[i + 1][j + 1]

                else:
                    # 删除 word1[i]
                    delete = dp[i + 1][j]

                    # 插入 word2[j]
                    insert = dp[i][j + 1]

                    # 把 word1[i] 替换成 word2[j]
                    replace = dp[i + 1][j + 1]

                    # 当前操作本身需要 1 次
                    dp[i][j] = 1 + min(
                        delete,
                        insert,
                        replace
                    )

        return dp[0][0]

        ## Time: O(mn)
        ## Space = O(mn)
        