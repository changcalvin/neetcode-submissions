class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            # 整个 word 都匹配完
            if i == len(word):
                return node.endOfWord
            
            c = word[i]  # 普通字符：沿对应 child 继续走
            if c != ".":
                if c not in node.children:
                    return False
                return dfs(i + 1, node.children[c])

            # "."：尝试当前节点的所有 children
            for child in node.children.values():
                if dfs(i + 1, child):
                    return True
            return False

        return dfs(0, self.root)

# 设 word 长度为 L：
    # addWord:
        # Time: O(L)
        # Space: O(L) worst case
    # search:
        # Time: O(L) normally
        # Worst Case: O(26^L)
        # Space: O(L)  # recursion