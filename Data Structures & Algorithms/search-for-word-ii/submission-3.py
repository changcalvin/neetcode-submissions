class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None 
        # 改 endOfWord = False 成 self.word = None 
        # 因为找到一个单词时，我们希望直接知道它是什么。


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # 把所有 words 放入 Trie
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word  # 记住这个单词

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            # 越界或者这个 cell 已经使用过
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] == "#"):
                return

            char = board[r][c]
            # 当前字符无法继续任何 Trie 中的 word
            if char not in node.children:
                return

            node = node.children[char]
            # 找到一个完整 word
            if node.word:
                res.append(node.word)
                node.word = None   # 防止重复加入答案
            
            # 标记当前 cell 已使用
            board[r][c] = "#"

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # backtracking
            board[r][c] = char

        # 每个 cell 都可以作为起点
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res

# 设：
# m × n = board 大小
# L = 最长 word 长度

# Time: O(m * n * 3^L) worst case
# Space: O(total characters in words + L)