class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ## hashset
        # nums[j] + nums[k] = -nums[i]

        res = set()

        n = len(nums)

        for i in range(n):

            seen = set()

            for j in range(i + 1, n):
                complement = -nums[i] - nums[j]

                if complement in seen:
                    triplet = tuple(sorted(
                        [nums[i], nums[j], complement]
                    ))
                    res.add(triplet)
                
                seen.add(nums[j])
        
        return [list(triplet) for triplet in res]

        ## time: O(n^2)
        ## space: O(n + k)


        
        