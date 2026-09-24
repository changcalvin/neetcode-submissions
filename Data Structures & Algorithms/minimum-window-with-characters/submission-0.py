class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        need = Counter(t)
        window = defaultdict(int)
        have = 0
        required = len(need)
        best_len = float('inf')
        best_start = 0
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                if right - left + 1 < best_len:
                    best_len = right-left+1
                    best_start = left
            
                d = s[left]
                window[d] -= 1
                if d in need and window[d] < need[d]:
                    have -= 1
                left += 1
        
        return "" if best_len == float("inf") else s[best_start:best_start + best_len]


