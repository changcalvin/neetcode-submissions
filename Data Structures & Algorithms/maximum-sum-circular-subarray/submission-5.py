class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum, maxSum = nums[0], nums[0]
        curMin, curMax = 0, 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin +n, n)
            total += n
            maxSum = max(curMax, maxSum)
            minSum = min(curMin, minSum)
        
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum