class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last：记录每个字符最后一次出现的 index
        last = {}
        
        for i in range(len(s)):
            last[s[i]] = i

        # res：保存每个 substring 的长度
        res = []
        # start：当前 substring 的起点
        # end：当前 substring 必须覆盖的最右位置
        start = 0
        end = 0

        for i in range(len(s)):
            # 当前字符最后出现的位置可能更远
            # 所以需要更新当前 substring 的右边界
            end = max(end, last[s[i]])
            # 所有已遇到字符的最后出现位置都已覆盖
            # 可以在这里切分，保证 substring 尽可能短
            if i == end:
                # 计算当前 substring 的长度
                res.append(end - start + 1)
                # 下一个 substring 从 i + 1 开始
                start = i + 1

        return res