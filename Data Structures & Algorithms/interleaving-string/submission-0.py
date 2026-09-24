class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        ## 2D Bottom-up DP

        m = len(s1)
        n = len(s2)

        # 长度必须正好相加
        if m + n != len(s3):
            return False

        # dp[i][j] 表示：s1[i:] 和 s2[j:] 能否组成 s3[i + j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 三个字符串都已经使用完，匹配成功
        dp[m][n] = True

        # 从右下往左上计算，
        # 因为当前状态依赖 dp[i+1][j] 和 dp[i][j+1]
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):

                # 右下角已经初始化，不需要重复处理
                if i == m and j == n:
                    continue

                # 选择 1：
                # 如果 s1 当前字符能匹配 s3[k]，
                # 并且剩余部分也可以匹配，则当前状态为 True
                use_s1 = (
                    i < m
                    and s1[i] == s3[i + j]
                    and dp[i + 1][j]
                )

                # 选择 2：
                # 如果 s2 当前字符能匹配 s3[k]，
                # 并且剩余部分也可以匹配，则当前状态为 True
                use_s2 = (
                    j < n
                    and s2[j] == s3[i + j]
                    and dp[i][j + 1]
                )

                # 只要任意一种选择可行即可
                dp[i][j] = use_s1 or use_s2

        return dp[0][0]

        ## Time: O(mn)
        ## Space = O(mn)

