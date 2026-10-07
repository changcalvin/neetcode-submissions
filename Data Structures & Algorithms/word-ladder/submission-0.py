class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        # endWord 必须存在于 wordList
        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            # 尝试修改 word 的每一个位置
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word in words:
                        # 加入 BFS
                        queue.append((new_word, length + 1))
                        # 删除 = 标记 visited，避免重复访问
                        words.remove(new_word)

        return 0

# N = wordList 中单词数量
# L = 每个单词长度

# 对于每个单词：L 个位置 × 26 个字母
# 而 Python 中：word[:i] + ch + word[i + 1:]
# 创建新字符串本身需要 O(L)。
# 所以严格来说：Time: O(N * 26 * L^2) = O(N * L^2)
# Space: O(N)

# 面试时可以直接说：
# Time: O(N * L^2)
# Space: O(N)