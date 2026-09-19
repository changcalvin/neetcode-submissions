class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0,nums)
    
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
                if j < len(p) and p[j] == nums[i]:
                    break
        return resPerms