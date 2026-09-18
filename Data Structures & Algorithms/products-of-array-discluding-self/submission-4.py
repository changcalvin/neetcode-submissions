class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefixRight = []
        prefixLeft = [0] * l
        curRight = 1
        curLeft = 1

        for n in nums:
            curRight = curRight * n
            prefixRight.append(curRight)

        for i in range(l-1, -1, -1):
            curLeft = curLeft * nums[i]
            prefixLeft[i] = curLeft

        res = []
        for i in range(l):
            right = prefixLeft[i+1] if i+1 < l else 1
            left = prefixRight[i-1] if i-1 >= 0 else 1
            res.append(right * left)
        return res