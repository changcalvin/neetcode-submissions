class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ## Sorting

        groups = defaultdict(list)

        for s in strs:
            # sorted(s) 返回 list，不能直接作为 dictionary key
            # 转成 tuple 后可以作为 hashable key
            key = tuple(sorted(s))

            groups[key].append(s)

        return list(groups.values())

        # n: 字符串数量
        # k: 字符串的平均/最大长度

        ## Time: O(n · k log k)
            # 每个字符串：
            # - sorted(s) → O(k log k)
            # - n 个字符串 → O(nk log k)

        ## Space: O(nk)
            # - sorted representation / keys → 最多 O(nk)
            # - HashMap grouping → O(n) references
            # - output → O(nk)，如果计算字符串内容