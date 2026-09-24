class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ## 1D Bottom-up DP

        # dp[a] 表示：凑出金额 a 所需要的最少 coin 数
        #
        # amount + 1 表示一个“不可能的较大值”
        # 因为最差情况下用面值 1，也最多只需要 amount 个 coin
        dp = [amount + 1] * (amount + 1)

        # 凑出金额 0 不需要任何 coin
        dp[0] = 0

        # 从较小金额开始，逐步推出更大的金额
        for a in range(1, amount + 1):
            for coin in coins:
                # 只有当前金额足够放入这个 coin 时才能转移
                if coin <= a:
                    dp[a] = min(
                        dp[a],
                        dp[a - coin] + 1
                    )

        # 如果仍然是初始的大值，说明无法凑出 amount
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]


        # C = len(coins)
        # A = amount

        ## Time: O(A × C)
            # 外层遍历所有金额：1 ... amount → O(A)
            # 对于每个金额，遍历所有 coins：O(C)
            # 所以：O(A × C)
        ## Space: O(A)
            # dp：O(A)
            # 其他变量：O(1)
            # 所以最终：Space = O(A)