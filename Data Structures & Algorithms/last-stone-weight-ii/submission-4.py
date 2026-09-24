class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

    # group1 sum = S1
    # group2 sum = S2

    # S1 + S2 = total
    # |S1 - S2| = |total - 2 * S1|
    # 希望 S1 尽可能接近：total / 2
    # 问题转化成: 选一些石头，使它们的总重量不超过 total // 2，并且尽可能大。

    ## 1D Bottom-up DP

        total = sum(stones)
        target = total // 2

        # dp[s] 表示：
        # 是否可以从目前处理过的 stones 中选出一些，使总和刚好为 s
        dp = [False] * (target + 1)

        # 什么都不选，可以组成重量 0
        dp[0] = True

        for stone in stones:
            # 0/1 Knapsack：
            # 每块 stone 只能使用一次，所以必须倒序更新
            for s in range(target, stone - 1, -1):
                if dp[s - stone]:
                    dp[s] = True

        # 从 target 往下找最大的可达重量
        for s in range(target, -1, -1):
            if dp[s]:
                # 两组分别是 s 和 total - s
                return total - 2 * s
    
    ## Time: O(n × target)
        # 外层 n 个 stones，内层最多遍历：target 个状态，O(n × target)
        # 最后从 target 往下找答案：O(target)
    ## Space: O(target)
        # dp：O(target)
        # 其他变量：O(1)

        