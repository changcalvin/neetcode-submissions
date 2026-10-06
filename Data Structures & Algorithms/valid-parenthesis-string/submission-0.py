class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        left = []

        for i, par in enumerate(s):
            if par == '(':
                left.append(i)
            elif par == '*':
                stack.append(i)
            else:
                if not left and not stack:
                    return False
                if left:
                    left.pop()
                else:
                    stack.pop()
        
        while left and stack:
            if left.pop() > stack.pop():
                return False
        
        return not left
                
