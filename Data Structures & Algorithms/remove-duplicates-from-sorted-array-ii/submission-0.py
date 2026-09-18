class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        k = 0
        pt = 0

        while pt < len(nums):
            if nums[pt] in seen and seen[nums[pt]] == 2:
                pt += 1
            else:
                seen[nums[pt]] += 1
                nums[k] = nums[pt]
                k += 1
                pt += 1
        return k