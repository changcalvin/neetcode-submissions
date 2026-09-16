class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        L = 0
        res = float('inf')

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                res = min(res, R-L+1)
                total -= nums[L]
                L += 1
            
        return 0 if res == float('inf') else res