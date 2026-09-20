class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        visit = {}
        res = []

        for i in range(len(words)-1):
            cur_word = words[i]
            next_word = words[i+1]
            minLen = min(len(cur_word), len(next_word))
            if len(cur_word) > len(next_word) and cur_word[:minLen] == next_word[:minLen]:
                return ""
            for j in range(minLen):
                if cur_word[j] != next_word[j]:
                    adj[cur_word[j]].add(next_word[j])
                    break
        
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
            