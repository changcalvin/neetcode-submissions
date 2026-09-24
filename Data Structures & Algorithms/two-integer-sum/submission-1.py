class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, n in enumerate(nums):
            if (target-n) in memo:
                return [memo[target-n], i]
            memo[n] = i
        return [-1, -1]
