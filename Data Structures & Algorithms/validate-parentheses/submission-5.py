class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch =='[':
                stack.append(ch)
            elif not stack:
                return False
            else:
                if ch == '}' and stack[-1] == '{':
                    stack.pop()
                elif ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
                    