class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        def notAlpha(char):
            return not ((ord('0') <= ord(char) <= ord('9')) or 
            (ord('a') <= ord(char.lower()) <= ord('z')))

        while left < right:
            while left < right and notAlpha(s[left]):
                left += 1
            while left < right and notAlpha(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True