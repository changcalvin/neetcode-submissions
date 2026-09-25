class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # hashmap

        # last_seen[char] = 这个字符最近一次出现的 index
        last_seen = {}

        left = 0
        longest = 0

        for right, char in enumerate(s):
            # 只有 duplicate 位于当前 window 内，才需要移动 left
            if char in last_seen and last_seen[char] >= left:
                # 直接跳到旧 duplicate 的下一个位置
                left = last_seen[char] + 1

            # 无论是否重复，都更新 char 最近出现的位置
            last_seen[char] = right

            # 当前 window 一定没有 duplicate
            longest = max(longest, right - left + 1)

        return longest

        # C: character set 的大小

        # time: O(n)
        # space: O(n), 更准确的 O(min(n, C))