class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        self.helper(0, nums, [], 0, combs, target)
        return combs

    def helper(self, i, nums, curCombs, curVal, combs, target):
        if curVal == target:
            combs.append(curCombs.copy())
            return
        elif curVal > target:
            return
    
        for j in range(i, len(nums)):
            curCombs.append(nums[j])
            self.helper(j, nums, curCombs, curVal+nums[j], combs, target)
            curCombs.pop()
    