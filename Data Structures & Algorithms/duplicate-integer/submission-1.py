class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)

        for n in nums:
            if n in counter:
                return True
            counter[n] = 1
        return False

