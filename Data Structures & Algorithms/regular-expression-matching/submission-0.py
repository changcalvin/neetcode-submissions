class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j]：s 前 i 个字符与 p 前 j 个字符是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 两个空字符串可以匹配
        dp[0][0] = True

        # 初始化：s 为空时，p 可能通过 x* 匹配 0 次
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # 从短前缀逐步计算更长前缀
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if p[j - 1] == '*':
                    # 选择 1：x* 匹配 0 次
                    dp[i][j] = dp[i][j - 2]

                    # 选择 2：x* 匹配至少 1 次
                    # 当前字符必须与 * 前面的字符匹配
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

                else:
                    # 普通字符或 .：必须匹配当前字符
                    if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]

        # 两个字符串的全部字符是否匹配
        return dp[m][n]