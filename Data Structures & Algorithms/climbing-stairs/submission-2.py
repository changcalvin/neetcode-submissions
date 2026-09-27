class Solution:
    def climbStairs(self, n: int) -> int:
        
        ## Top-down DFS + Memoization

        # memo[i] = 从第 i 阶出发，到达 n 的方法数
        memo = {}

        def dfs(i):
            # base case 1：
            # 正好走到终点，这是一种有效方案
            if i == n:
                return 1

            # base case 2：
            # 超过终点，这不是有效方案
            if i > n:
                return 0

            # 避免重复计算相同 state
            if i in memo:
                return memo[i]

            # 当前可以选择走 1 step 或 2 steps
            memo[i] = dfs(i + 1) + dfs(i + 2)

            return memo[i]

        return dfs(0)

        ## Time: O(n)
        ## Space: O(n)