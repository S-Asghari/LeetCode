class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1] # base marker
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else: # c == ')'
                stack.pop()
                if len(stack) == 0:
                    stack.append(i) # We push i as the new base marker, since nothing before or including this point can be part of a valid substring going forward.
                else:
                    ans = max(ans, i - stack[-1])

        return ans