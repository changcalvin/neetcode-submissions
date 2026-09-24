class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        ## 2D Bottom-up DP
       

        # dp[i][j]：在最多使用 i 个 0、j 个 1 的情况下，最多可以选择多少个字符串。
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            # 统计当前字符串需要多少个 0 和 1
            zeros = s.count('0')
            ones = s.count('1')

            # 处理一个字符串 (zeros, ones) 时：
            # - 不选：dp[i][j] 不变
            # - 选：从之前的 dp[i - zeros][j - ones] 转移过来，再 +1

            # 每个字符串只能使用一次，所以两个 capacity 都要倒序
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i - zeros][j - ones] + 1
                    )
        
        return dp[m][n]

        ## Time: O(L × (K + mn))
            # L = len(strs)
            # 每个字符串长度最多记为 K。统计每个字符串的 0/1：O(K)
            # 对每个字符串，需要遍历 m × n 个 DP 状态。
        ## Space: O(mn)
            # dp = O(mn)
            # 除此之外只有：zeros, ones = O(1)




        