class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            for L, R in ((i, i), (i, i + 1)):
                while L >= 0 and R < len(s) and s[L] == s[R]:
                    if (R - L + 1) > len(res):
                        res = s[L:R+1]
                    L -= 1
                    R += 1

        return res