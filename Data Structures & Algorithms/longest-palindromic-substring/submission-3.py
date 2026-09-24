class Solution:
    def longestPalindrome(self, s: str) -> str:

        ## 2D Bottom-up DP
        
        n = len(s)

        # dp[i][j] 表示：s[i:j+1] 是否是回文串
        dp = [[False] * n for _ in range(n)]

        best_start = 0
        best_len = 1

        # 从后往前枚举 i，保证 dp[i+1][j-1] 已经计算好
        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                # 当前两端字符必须相同
                if s[i] == s[j]:

                    # 长度 <= 2 时：
                    # "a" 或 "aa" 只要两端相同就是回文
                    #
                    # 长度 > 2 时：
                    # 中间部分也必须是回文
                    if j - i <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        cur_len = j - i + 1

                        if cur_len > best_len:
                            best_len = cur_len
                            best_start = i

        return s[best_start:best_start + best_len]
        
        ## Time = O(n²)
        ## Space = O(n²)