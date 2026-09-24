class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0
        res = 1 if nums else 0

        skip = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                skip += 1
            elif nums[i] == nums[i-1]+1:
                res = max(res, i-prev+1-skip)
            else:
                skip = 0
                prev = i
        return res