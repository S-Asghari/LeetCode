class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Brute-Force
        n, m = len(haystack), len(needle)
        if m == 0: return 0
        for i in range(0, n-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1