class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ## top-down DP: DFS + Memoization

        # memo[(i, current_sum)]:
        # 从第 i 个数字开始，在当前和为current_sum 时，最终能组成 target 的方法数量

        memo = {}

        def dfs(i, current_sum):
            if i == len(nums):
                if current_sum == target:
                    return 1
                return 0
            
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]
            
            add = dfs(i + 1, current_sum + nums[i])

            subtract = dfs(i + 1, current_sum - nums[i])

            memo[(i, current_sum)] = add + subtract

            return memo[(i, current_sum)]
        
        return dfs(0, 0)

        # n = len(nums)
        # S = sum(nums), current_sum = O(S)

        ## TIME
            # (i, current_sum): O(nS)
        ## TOTAL: O(nS)

        ## SPACE
            # memo: O(nS)
            # dfs: O(n)
        ## TOTAL: O(nS)



            
