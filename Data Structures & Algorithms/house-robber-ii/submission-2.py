class Solution:
    def rob(self, nums: List[int]) -> int:
        # Boundary case：
        # 如果只有一个 house，直接 rob 它。
        # 这个必须单独处理，否则 nums[:-1] 和 nums[1:]
        # 都会变成空数组。
        
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            # prev2 = 考虑到前前一个 house 时的最大金额
            # prev1 = 考虑到前一个 house 时的最大金额
            prev2 = 0
            prev1 = 0

            for money in houses:
                # 两种选择：
                # 1. rob 当前 house：
                #    不能 rob 前一个，所以是 prev2 + money
                # 2. skip 当前 house：
                #    保留之前的最优结果 prev1
                current = max(
                    prev2 + money,
                    prev1
                )

                # 滚动更新 DP states
                prev2 = prev1
                prev1 = current

            return prev1

        # 因为 first 和 last 不能同时 rob：
        #
        # Case 1: exclude last house
        # Case 2: exclude first house
        #
        # 两种情况分别变成普通 House Robber I
        return max(
            rob_line(nums[:-1]),
            rob_line(nums[1:])
        )


        ## Time: O(n)
        ## Space: O(n) # Python slicing 会创建新的 list