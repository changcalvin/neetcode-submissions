class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        ## Top-down DFS + Memo
        
        # dfs(i, current_sum)表示：
            # 处理到第 i 块 stone 时，
            # 当前 signed sum 是 current_sum，
            # 最后能得到的最小绝对值是多少。
        
        memo = {}

        def dfs(i, current_sum):
            # 所有 stone 都决定完正负号
            if i == len(stones):
                return abs(current_sum)

            state = (i, current_sum)

            if state in memo:
                return memo[state]

            # 当前 stone 放到正组
            add = dfs(
                i + 1,
                current_sum + stones[i]
            )

            # 当前 stone 放到负组
            subtract = dfs(
                i + 1,
                current_sum - stones[i]
            )

            memo[state] = min(add, subtract)

            return memo[state]

        return dfs(0, 0)

    ## Time = O(n × total)
        # current_sum 的范围：-total 到 total，所以有：O(total)种不同 sum。
        # 状态：(i, current_sum) 最多：O(n × total)

    ## Space = O(n × total)
        # memo = O(n × total)
        # 递归栈 = O(n)

