class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        res = nums[0]

        for num in nums[1:]:
            prev_max = cur_max
            prev_min = cur_min

            cur_max = max(num, num * prev_max, num * prev_min)
            cur_min = min(num, num * prev_max, num * prev_min)

            res = max(res, cur_max)

        return res

# Time: O(n)
# Space: O(1)