class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        def hours(k):
            res = 0
            for p in piles:
                res += math.ceil(p/k)
            return res

        while left < right:
            k = (left+right)//2
            totalTime = hours(k)
            if totalTime <= h:
                res = k
                right = k
            else:
                left = k+1
        return res
            
