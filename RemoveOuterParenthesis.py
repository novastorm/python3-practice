class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = []
        for c in S:
            if c == '(':
                stack.append(c)
                if len(stack) == 1: 
                    continue
            if c == ')':
                stack.pop()
                if not stack:
                    continue
            result.append(c)
        return ''.join(result)
    