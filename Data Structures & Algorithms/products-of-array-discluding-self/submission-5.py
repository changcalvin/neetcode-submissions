class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre = []
        post = [1] * length
        
        cur = 1
        for n in nums:
            cur = cur * n
            pre.append(cur)
        
        post[length-1] = nums[length-1]
        for i in range(length-2, -1, -1):
            post[i] = nums[i] * post[i+1] 
        
        res = []
        for i in range(length):
            if i-1 < 0:
                res.append(post[i+1])
                continue
            if i+1 >= length:
                res.append(pre[i-1])
                continue
            res.append(pre[i-1] * post[i+1])
        return res
