class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = [0] * 27
        string2 = [0] * 27

        for c in s:
            string1[(ord(c) - ord('a'))] += 1
        for c in t:
            string2[(ord(c) - ord('a'))] += 1
        
        for i in range(27):
            if string1[i] != string2[i]:
                return False
        return True