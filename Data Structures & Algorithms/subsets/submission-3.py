class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet = []
        subSet = []
        self.helper(0, nums, curSet, subSet)
        return subSet

    def helper(self, i, nums, curSet, subSet):
        if i >= len(nums):
            subSet.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(i + 1, nums, curSet, subSet)
        curSet.pop()

        self.helper(i + 1, nums, curSet, subSet)
