class Solution:
    def rob(self, nums: List[int]) -> int:
        
        ## Top-down DFS + Memo

        if len(nums) == 1:
            return nums[0]

        def rob_range(left, right):
            # memo[i] = 从 i 开始，在 [left, right) 内能 rob 的最大金额
            memo = {}

            def dfs(i):
                # Base case：超出当前 linear range
                if i >= right:
                    return 0

                if i in memo:
                    return memo[i]

                # rob 当前 house → 跳过下一家
                rob_current = nums[i] + dfs(i + 2)

                # skip 当前 house
                skip_current = dfs(i + 1)

                memo[i] = max(rob_current, skip_current)
                return memo[i]

            return dfs(left)

        n = len(nums)

        return max(
            rob_range(0, n - 1),  # exclude last
            rob_range(1, n)       # exclude first
        )

        # Time: O(n)
        # Space: O(n)