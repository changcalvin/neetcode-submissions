class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ## Bottom-up DP + HASHMAP

        # dp[s]: 目前已经处理过的数字，组成 sum = s 有多少种方法
        dp = {0: 1}

        for num in nums:
            next_dp = {}
            # 为什么要建 next_dp？
            # 因为当前这个 num 必须恰好使用一次。
            # 我们要从“上一轮的状态”生成“这一轮的新状态”，不能边读旧 dp 边修改它。

            for current_sum, count in dp.items():
                # add
                add_num = current_sum + num
                next_dp[add_num] = next_dp.get(add_num, 0) + count
                # subtract
                subtract_sum = current_sum - num
                next_dp[subtract_sum] = (
                    next_dp.get(subtract_sum, 0) + count
                )
            
            dp = next_dp
        
        return dp.get(target, 0)

        
        # n = len(nums)
        # S = sum(nums), current_sum = O(S)
        
        # time: O(nS)
        # space: O(S)
        
        


        