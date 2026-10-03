class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {} # need[ch]: t 中字符 ch 需要出现多少次
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        window = {} # window[ch]: 当前 sliding window 中 ch 出现多少次
        have = 0 # have: 当前已经满足 frequency 要求的字符种类数
        need_count = len(need) # need_count: 总共需要满足的字符种类数
        left = 0
        res = [-1, -1] # 保存目前最短窗口 [start, end]
        min_len = float("inf")

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            
            if ch in need and window[ch] == need[ch]:
                have += 1 # 只有“刚好达到要求”时 have 才 +1

            # 当前窗口已经满足 t：尽可能移动 left，寻找更短的有效窗口
            while have == need_count:
                # 先记录当前有效窗口
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = [left, right]

                # 移除最左边字符
                left_ch = s[left]
                window[left_ch] -= 1

                # 如果移除后不再满足该字符要求，窗口失效
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        if min_len == float("inf"):
            return "" # 没有找到任何有效窗口

        start, end = res
        return s[start:end + 1]