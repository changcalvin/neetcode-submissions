class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        ## 2D Bottom-up DP
        
        c = len(coins)

        # dp[i][a] 表示：
        # 使用前 i 种 coin，凑出金额 a 的组合数量
        dp = [
            [0] * (amount + 1)
            for _ in range(c + 1)
        ]

        # 凑出金额 0 都有 1 种方式：
        # 什么 coin 都不选
        for i in range(c + 1):
            dp[i][0] = 1


        for i in range(1, c + 1):
            coin = coins[i - 1]

            for a in range(1, amount + 1):

                # 情况 1：完全不使用当前 coin
                dp[i][a] = dp[i - 1][a]

                # 情况 2：至少使用一个当前 coin
                if coin <= a:
                    dp[i][a] += dp[i][a - coin]

        return dp[c][amount]

    ## Time = O(CA)
        # 二维 table 大小：(C + 1) × (A + 1)
        # 所以：Time = O(CA)

    ## Sppace = O(CA)
        # dp = O(CA)
        # 所以：Space = O(CA)