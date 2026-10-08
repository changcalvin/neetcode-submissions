class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 题目保证 nums 非空
        # 初始化为第一个元素，避免全负数时错误返回 0
        cur_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # 以 i 结尾的最大和：
            # 继续之前的 subarray，或者从 nums[i] 重新开始
            cur_sum = max(nums[i], cur_sum + nums[i])
            # 更新全局最大 subarray sum
            max_sum = max(max_sum, cur_sum)

        return max_sum

# Time: O(n)
# Space: O(1)