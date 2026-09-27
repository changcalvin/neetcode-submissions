class Solution:
    def rob(self, nums: List[int]) -> int:
        
        ## Bottom-up DP + O(1) Space
        
        # prev2 = 考虑到前前一个 house 时的最大金额
        # prev1 = 考虑到前一个 house 时的最大金额
        #
        # 初始化为 0：
        # 在还没有考虑任何 house 时，最大金额是 0
        prev2 = 0
        prev1 = 0

        for money in nums:
            # 对当前 house 有两个选择：
            #
            # 1. rob 当前 house：
            #    前一个 house 不能 rob
            #    => prev2 + money
            #
            # 2. skip 当前 house：
            #    => 保留之前的最优解 prev1
            current = max(prev2 + money, prev1)

            # 滚动更新两个 DP state
            prev2 = prev1
            prev1 = current

        return prev1

        ## Time: O(n)
        ## Space: O(1)