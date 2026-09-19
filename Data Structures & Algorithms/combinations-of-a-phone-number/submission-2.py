class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if not digits:
            return []

        strings = []
        for ch in digits:
            strings.append(phone[ch])
        combs = []
        self.helper(0, strings, [], combs)
        return combs

    def helper(self, i, strings, curComb, combs):
        if i == len(strings):
            combs.append("".join(curComb))
            return

        for letter in strings[i]:
            curComb.append(letter)
            self.helper(i + 1, strings, curComb, combs)
            curComb.pop()
        