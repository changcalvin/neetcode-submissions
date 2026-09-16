class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        window = sum(arr[:k])
        count = 1 if window >= target else 0

        for i in range(k, len(arr)):
            window += arr[i] - arr[i - k]
            if window >= target:
                count += 1
        return count
        
            