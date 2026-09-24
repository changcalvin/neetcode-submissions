class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        ## Top-down DFS + Memoization

        # 三种票的有效天数：
        # costs[0] -> 1-day
        # costs[1] -> 7-day
        # costs[2] -> 30-day
        durations = [1, 7, 30]

        # memo[i] 表示：
        # 从 days[i] 这个旅行日开始，
        # 覆盖后面所有旅行日所需要的最小费用
        memo = {}

        def dfs(i): # 从 days[i] 开始，还没有被覆盖的所有旅行日，最少需要花多少钱。
            # Base case：
            # 所有旅行日都已经被覆盖，不需要再花钱
            if i == len(days):
                return 0

            # 相同状态已经计算过，直接返回
            if i in memo:
                return memo[i]

            min_cost = float("inf")

            # 尝试购买三种不同的 pass
            for duration, ticket_cost in zip(durations, costs):

                # 当前 pass 从 days[i] 当天开始生效
                # 能覆盖到 days[i] + duration - 1
                #
                # 所以第一个不能被覆盖的日期需要满足：
                # days[j] >= days[i] + duration
                j = i

                while (
                    j < len(days)
                    and days[j] < days[i] + duration
                ):
                    j += 1

                # 当前买这张票，
                # 再加上从第 j 个旅行日开始的最优费用
                total_cost = ticket_cost + dfs(j)

                min_cost = min(min_cost, total_cost)

            memo[i] = min_cost
            
            return min_cost

        return dfs(0)




        # 设：N = len(days)
    
    ## Time: O(N²)
        # 一共有：O(N)个不同状态 dfs(i)。
        # 每个状态尝试：3 种 ticket
        # 但是当前代码为了找下一未覆盖日期，用了：while ...
        # 最坏每次可能向后扫 O(N)。
        # 所以严格按这版代码： Time: O(N²)
        # 因为：O(N) states × 3 tickets × O(N) scan
        # 三种票是常数，所以：O(N²)

    ## Space: O(N)
        # memo：O(N)
        # 递归栈最深：O(N)
        # 因此：Space: O(N)
        # 不过这里 days.length 很小，而且一年最多 365 天，所以已经完全足够。