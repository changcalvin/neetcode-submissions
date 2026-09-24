class Solution:
    def countSubstrings(self, s: str) -> int:

        ## 2D Bottom-up DP

        n = len(s)

        # dp[i][j] 表示：s[i:j+1] 是否是回文子串
        dp = [[False] * n for _ in range(n)]

        count = 0

        # 从后往前枚举左边界，保证 dp[i+1][j-1] 已经计算好
        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                # 两端字符必须相同
                if s[i] == s[j]:

                    # 长度为 1 或 2 时，两端相同就已经是 palindrome
                    # 长度更长时，中间部分也必须是 palindrome
                    if j - i <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        # 每个 True 状态对应一个回文子串
                        count += 1

        return count

        ## Time = O(n²)
        ## Space = O(n²)
        