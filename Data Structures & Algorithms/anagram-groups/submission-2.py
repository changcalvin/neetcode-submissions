class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        # key: 26个字母的频率特征
        # value: 具有相同特征的所有字符串

        for s in strs:
            count = [0] * 26

            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)

            if key not in groups:
                groups[key] = []
            
            groups[key].append(s)

        return list(groups.values())

        # n: 字符串数量
        # k: 字符串的平均/最大长度

        ## time: O(nk)
            # 对于每一个字符串：
                # count：1
                # 遍历字符串统计frequency：k
                # tuple（count）：1

        ## space: O(nk)

        