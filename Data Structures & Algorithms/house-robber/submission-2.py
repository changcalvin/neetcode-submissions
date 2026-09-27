class Solution:
    def rob(self, nums: List[int]) -> int:
        
        ## Top-down DFS + Memoization
        
        # memo[i] = 从 house i 开始能够 rob 的最大金额
        memo = {}

        def dfs(i):
            # Base case：
            # 已经超过最后一个 house，没有钱可以继续 rob
            if i >= len(nums):
                return 0

            # 当前 state 已经计算过，直接复用
            if i in memo:
                return memo[i]

            # Option 1: rob 当前 house
            # 因为不能 rob adjacent house，所以跳到 i + 2
            rob_current = nums[i] + dfs(i + 2)

            # Option 2: skip 当前 house
            skip_current = dfs(i + 1)

            memo[i] = max(rob_current, skip_current)

            return memo[i]

        return dfs(0)

        ## Time: O(n)
        ## Space: O(n)