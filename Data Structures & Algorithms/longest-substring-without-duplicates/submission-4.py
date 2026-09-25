class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # hashset
        window = set()

        left = 0
        longest = 0
        
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])

            longest = max(longest, right - left + 1)
        
        return longest

        # C: character set 的大小

        # time: O(n)
        # space: O(n), 更准确的 O(min(n, C))


        