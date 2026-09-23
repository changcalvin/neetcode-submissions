class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        ## 1D DP
        # dp[s]: 是否可以用已经处理过的数字组成 sum = s

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)

        dp[0] = True

        # when num: if dp[s - num] = True, then dp[s] = True
        for num in nums:
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True
            
            if dp[target]:
                return True
        
        return dp[target]

        # time: O(n * target)
            # 外层遍历 n 个 nums, 每个数字最多遍历 target 个状态，所以 O(n × target)
        # space: O(target)
            # dp：O(target)；其他变量：O(1)

        