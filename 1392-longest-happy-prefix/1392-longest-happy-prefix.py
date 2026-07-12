class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        prefix = 0
        suffix = 0
        base = 29
        power = 1
        mod = 10 ** 9 + 7
        longest_prefix = ""
        for i in range(n-1):
            p_char = ord(s[i]) - ord('a') + 1
            s_char = ord(s[n-i-1]) - ord('a') + 1
            prefix = ((prefix * base) % mod + p_char) % mod
            suffix = (suffix + (s_char * power) % mod) % mod
            power = (power * base) % mod
            if prefix == suffix:
                longest_prefix = s[:i+1]
        return longest_prefix