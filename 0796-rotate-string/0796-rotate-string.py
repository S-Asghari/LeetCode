class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        n = len(goal)
        i = 0
        while i < n:
            s_prime = s[i:] + s[:i]
            if s_prime == goal:
                return True
            i += 1
        return False