class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = ['+', '-', '*', '/']

        for t in tokens:
            if t not in oper:
                stack.append(int(t))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if t == '+':
                    stack.append(val2 + val1)
                if t == '-':
                    stack.append(val2 - val1)
                if t == '*':
                    stack.append(val2 * val1)
                if t == '/':
                    stack.append(int(val2 / val1))
        
        return stack[-1] if stack else 0
                
            
            