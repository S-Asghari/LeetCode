class Solution:
    def checkMatch(self, c1: str, c2: str) -> bool:
        if c1 == '(' and c2 == ')': return True  
        if c1 == '[' and c2 == ']': return True 
        if c1 == '{' and c2 == '}': return True
        return False

    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack: return False
                if not self.checkMatch(stack.pop(), s[i]): return False
        return True if not stack else False