class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        # 两个关键点：
            # 第一，每个 coin 可以无限使用，所以仍然是 Unbounded Knapsack。
            # 第二，题目数的是 combination，不是 permutation。

        ## 1D Bottom-up DP
        
        # dp[a]表示：使用目前已经处理过的 coin，凑出金额 a 的组合数。
        dp = [0] * (amount + 1)

        # 凑出金额 0 有 1 种方法：什么 coin 都不选
        dp[0] = 1

        # 外层遍历 coin，保证组合不会因为顺序不同而被重复计算
        # Combination → coin 在外层
        # Permutation → amount 在外层
        for coin in coins:

            # 当前 coin 可以无限使用，所以金额必须从小到大更新
            for a in range(coin, amount + 1):

                # 所有能组成 a - coin 的组合，
                # 再加入一个当前 coin，
                # 都可以组成金额 a
                dp[a] += dp[a - coin]

        return dp[amount]


        # 设：C = len(coins)，A = amount

        ## Time: O(C × A)
            # 外层遍历：C 个 coins
            # 每个 coin 最多遍历：A 个金额状态
            # 所以：O(C × A)

        ## Space: O(A)
            # dp：O(A)
            # 其他变量：O(1)
            # 所以最终：Space = O(A)