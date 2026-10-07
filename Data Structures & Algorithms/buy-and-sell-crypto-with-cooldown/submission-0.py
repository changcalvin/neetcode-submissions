class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # memo[(i, buying)]：记录当前状态下的最大利润
        memo = {}

        def dfs(i, buying):
            # Base case：超过最后一天
            if i >= n:
                return 0
            # 已经计算过，直接返回
            if (i, buying) in memo:
                return memo[(i, buying)]

            if buying:
                # 没有股票：买入 or 跳过
                buy = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)
                profit = max(buy, skip)
            else:
                # 持有股票：卖出 or 跳过
                # 卖出后 cooldown 一天，所以 i + 2
                sell = prices[i] + dfs(i + 2, True)
                skip = dfs(i + 1, False)
                profit = max(sell, skip)

            # 保存当前状态的最优结果
            memo[(i, buying)] = profit
            return profit

        # 第一天没有股票，可以买入
        return dfs(0, True)

        # Time: O(n)，Space: O(n)