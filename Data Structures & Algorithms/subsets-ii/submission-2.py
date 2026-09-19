class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subSet = []
        curSet = []
        nums.sort()
        self.helper(0, nums, curSet, subSet)
        return subSet
    
    def helper(self, i, nums, curSet, subSet):
        if i == len(nums):
            subSet.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(i+1, nums, curSet, subSet)
        curSet.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.helper(i+1, nums, curSet, subSet)
