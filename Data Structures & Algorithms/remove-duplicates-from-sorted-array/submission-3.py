class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()
        pt = 0
        while pt < len(nums):
            if nums[pt] in seen:
                pt += 1
            else:
                seen.add(nums[pt])
                nums[k] = nums[pt]
                k += 1
                pt += 1
        return k
