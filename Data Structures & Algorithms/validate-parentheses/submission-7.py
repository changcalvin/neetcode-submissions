class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        # key 是右括号，value 是对应的左括号
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:

            # 左括号：直接入栈
            if char not in pairs:
                stack.append(char)

            # 右括号：检查是否和栈顶匹配
            else:
                # stack 为空：没有左括号可以匹配
                if not stack:
                    return False

                # 栈顶左括号类型不匹配
                if stack[-1] != pairs[char]:
                    return False

                # 匹配成功，弹出栈顶
                stack.pop()

        # 最后 stack 必须为空
        return len(stack) == 0


        ## Time: O(n)
        ## Space: O(n)