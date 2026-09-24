class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        ## Bottom-up DP by Calendar Day

        # 用 set 可以 O(1) 判断某一天是不是旅行日
        travel_days = set(days)

        # 只需要计算到最后一个旅行日
        last_day = days[-1]

        # dp[d] 表示：覆盖 day 1 ~ day d 所有旅行日的最小费用
        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):

            # 如果今天不旅行，
            # 不需要额外买票，费用和昨天一样
            if day not in travel_days:
                dp[day] = dp[day - 1]
                continue

            # 如果今天旅行，就考虑三种票

            # 1-day pass：
            # 覆盖今天，所以之前只需要覆盖到 day - 1
            cost_1 = dp[day - 1] + costs[0]

            # 7-day pass：
            # 可以覆盖 day-6 ~ day，
            # 所以只需要保证 day-7 之前已经覆盖
            cost_7 = dp[max(0, day - 7)] + costs[1]

            # 30-day pass：
            # 可以覆盖 day-29 ~ day
            cost_30 = dp[max(0, day - 30)] + costs[2]

            dp[day] = min(
                cost_1,
                cost_7,
                cost_30
            )

        return dp[last_day]


        
        # 设：N = len(days)
        # 最多只遍历：last_day <= 365 天。
        # 更一般地设：D = days[-1]


        ## Time: O(N + D)
            # Time：travel_days = set(days) → O(N)
            # 遍历 1...D → O(D)
            # 所以：Time: O(N + D)
            # 这题中 D <= 365。

        ## Space：O(N + D)
            # travel_days = O(N)
            # dp = O(D)
            # 所以：Space: O(N + D)