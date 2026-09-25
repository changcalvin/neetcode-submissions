class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1) // mid

            if total_hours <= h:
                right = mid
            
            else:
                left = mid + 1
        
        return left

        # n = len(piles)
        # M = max(piles)

        # time: O(nlogM)
        # space: O(1)


        