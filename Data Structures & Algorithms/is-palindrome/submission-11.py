class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        def isAlpha(ch):
            return ord('a') <= ord(ch.lower()) <= ord('z') or ord('0') <= ord(ch) <= ord('9')

        while left < right:
            while left < right and not isAlpha(s[left]):
                left += 1
            while right > left and not isAlpha(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
