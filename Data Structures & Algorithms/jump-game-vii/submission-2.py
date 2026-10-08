class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False

        dp = [False] * n
        dp[0] = True
        j = 0

        for i in range(n):
            if dp[i] == False:
                continue
            j = max(j, i+minJump)
            while j < min(i+maxJump+1, n):
                if s[j] == '0':
                    dp[j] = True
                j += 1
    
        return dp[n-1]