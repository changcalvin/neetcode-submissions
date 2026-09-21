class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            for L, R in ((i, i), (i, i+1)):
                while L >= 0 and R < len(s) and s[L] == s[R]:
                    res += 1
                    L -= 1
                    R += 1
                    
        return res