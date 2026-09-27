class Solution:
    def climbStairs(self, n: int) -> int:
        
        ## Bottom-up DP + O(1) Space

        # 根据题目 constraints，n >= 1
        # 如果面试官允许 n = 0，需要先确认如何定义答案

        # one = dp[i - 1]
        # two = dp[i - 2]
        #
        # base cases:
        # dp[1] = 1：只有 [1]
        # dp[2] = 2：[1,1], [2]
        if n <= 2:
            return n

        two = 1   # dp[1]
        one = 2   # dp[2]

        # 从 dp[3] 一直计算到 dp[n]
        for i in range(3, n + 1):

            # 到达 i：
            # 最后一步要么从 i-1 走 1 step，
            # 要么从 i-2 走 2 steps
            current = one + two

            # 滚动更新：
            # 原来的 dp[i-1] 变成下一轮的 dp[i-2]
            two = one

            # 当前 dp[i] 变成下一轮的 dp[i-1]
            one = current

        return one

        
        # Time: O(n)
        # Space: O(1)