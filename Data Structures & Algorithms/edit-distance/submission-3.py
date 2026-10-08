class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = {}

        def check(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in dp:
                return dp[(i, j)]
            
            if word1[i] == word2[j]:
                dp[(i, j)] = check(i+1, j+1)
            else:
                res = min(check(i+1, j), check(i, j+1))
                res = min(res, check(i+1, j+1))
                dp[(i, j)] = res + 1
            return dp[(i, j)]
        
        return check(0, 0)


        

        
        