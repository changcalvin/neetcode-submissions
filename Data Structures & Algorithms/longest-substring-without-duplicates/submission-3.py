class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            memo[s[right]] += 1
            while memo[s[right]] > 1:
                memo[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        
        return res
