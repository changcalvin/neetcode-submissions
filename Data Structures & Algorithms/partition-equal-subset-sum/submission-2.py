class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        ## top-down DP: Top-down DFS + Memoization

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        memo = {}

        def dfs(i, remain):
            # 已经成功组成 target
            if remain == 0:
                return True

            # 没有数字可用了，或者已经超过 target
            if i == len(nums) or remain < 0:
                return False

            # 相同状态不用重复计算
            if (i, remain) in memo:
                return memo[(i, remain)]

            # 选择当前 nums[i]
            take = dfs(i + 1, remain - nums[i])

            # 不选择当前 nums[i]
            skip = dfs(i + 1, remain)

            memo[(i, remain)] = take or skip

            return memo[(i, remain)]

        return dfs(0, target)

    ## Time = i * remain = O(n × target)
    ## Space = memo + 递归栈最深 = O(n × target) + O(n) = O(n × target)

        