class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixRight = []
        prefixLeft = []
        curRight = 0
        curLeft = 0

        for n in nums:
            curRight += n
            prefixRight.append(curRight)
        for i in range(len(nums)-1, -1, -1):
            curLeft += nums[i]
            prefixLeft.append(curLeft)

        prefixLeft.reverse()    
        for i in range(len(nums)):
            if prefixRight[i] == prefixLeft[i]:
                return i
        return -1