class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # grach[ch] saves which character must appear after ch
        graph = {ch: set() for word in words for ch in word}

        # indegree[ch] saves how many characters must appear before ch
        indegree = {ch: 0 for ch in graph}


        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
        

        queue = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)
        
        order = []

        while queue:
            ch = queue.popleft()
            order.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(order) != len(graph):
            return ''
        
        return ''.join(order)


        # C: 所有单词字符总数
        # V: 不同字符的数量(V < C)
        # E: 字母之间的先后关系

        ## time
            # 建立所有字符ch: O(C)
            # 比较相邻单词，扫描字符：O(C)
            # topological sort：O(V + E)
        ## total: O(C + E)

        ## space
            # graph: O(V + E)
            # indegree: O(V)
            # queue: O(V)
            # order: O(V)
        ## total: O(V + E)



        