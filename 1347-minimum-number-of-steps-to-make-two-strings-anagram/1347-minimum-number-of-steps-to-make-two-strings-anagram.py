class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_chars = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            s_chars[idx] += 1
        res = 0
        for c in t:
            idx = ord(c) - ord('a')
            s_chars[idx] -= 1
            if s_chars[idx] < 0:
                res += 1
        return res