class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 两端添加虚拟气球 1，统一处理边界
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[left][right]：
        # 戳破开区间 (left, right) 内所有气球的最大收益
        # Base case：区间内没有气球时，收益为 0
        dp = [[0] * n for _ in range(n)]

        # 按区间长度从小到大计算
        # 长度至少为 2，才可能包含一个气球
        for length in range(2, n):
            # 枚举区间左边界
            for left in range(n - length):
                right = left + length
                # 枚举区间内最后戳破的气球 k
                for k in range(left + 1, right):
                    # 左区间 + 右区间 + 最后戳破 k 的收益
                    coins = (
                        dp[left][k]
                        + dp[k][right]
                        + nums[left] * nums[k] * nums[right]
                    )

                    dp[left][right] = max(
                        dp[left][right], coins
                    )

        # 戳破所有真实气球，两个虚拟气球作为边界
        return dp[0][n - 1]

# 设原始数组有 N 个气球。
# Time: O(N³)
# Space: O(N²)