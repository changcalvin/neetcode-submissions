class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)
        
    def helper(self, i, nums):
        if i == len(nums):
            return [[]]
        
        resPerms = []
        perms = self.helper(i+1, nums)
        for p in perms:
            for j in range(len(p)+1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                resPerms.append(pCopy)
        return resPerms