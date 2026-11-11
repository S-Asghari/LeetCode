class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openning, closing = 0, 0 # '(', ')'
        result = []

        for c in s:
            if c == '(':
                openning += 1
                result.append(c)
            elif c == ')':
                if openning > closing:
                    closing += 1
                    result.append(c)
            else:
                result.append(c)
                
        i = len(result)-1
        while openning > closing and i >= 0:
            if result[i] == '(':
                del result[i]
                openning -= 1
            i -= 1

        return "".join(result)