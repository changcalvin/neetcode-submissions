class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        ## Bottom-up DP by Travel-Day Index
        
        n = len(days)

        durations = [1, 7, 30]

        # dp[i] 表示：
        # 从 days[i] 开始覆盖剩余所有旅行日的最小费用
        #
        # dp[n] 表示没有旅行日剩余，所以费用为 0
        dp = [0] * (n + 1)

        # 从最后一个旅行日往前计算
        for i in range(n - 1, -1, -1):
            min_cost = float("inf")

            # 尝试三种 pass
            for duration, ticket_cost in zip(durations, costs):
                j = i

                # 找到当前 pass 无法覆盖的第一个旅行日
                while (
                    j < n
                    and days[j] < days[i] + duration
                ):
                    j += 1

                # 当前票价
                # + 从第 j 个旅行日开始的最优费用
                total_cost = ticket_cost + dp[j]

                min_cost = min(
                    min_cost,
                    total_cost
                )

            dp[i] = min_cost

        return dp[0]


    ## Time: O(N²)
        # 和上面的 Top-down 版本一样，这版使用 while 找 j：
        # N 个 states × 3 种 pass × 最坏 O(N) 找下一个位置
        # 所以： Time: O(N²)
        
    ## Space：
        # dp = O(N)
        # 没有 recursion stack。
        # 所以：Space: O(N)