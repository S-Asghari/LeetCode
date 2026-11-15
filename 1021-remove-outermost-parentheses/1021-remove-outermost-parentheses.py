class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        primitives = []
        stack = []
        for j, c in enumerate(s):
            if c == '(':
                stack.append(j)
            else: # c is a ')'
                i = stack.pop()
                if not stack:
                    primitives.append((i, j))
        res = ""
        for pi, pj in primitives:
            res += s[pi+1: pj]
        return res