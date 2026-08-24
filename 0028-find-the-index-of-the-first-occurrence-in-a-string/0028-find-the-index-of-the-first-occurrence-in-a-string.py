from string import ascii_lowercase as chars
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # -----------
        # Brute-Force
        # -----------
        n, m = len(haystack), len(needle)
        if m == 0: return 0
        if n < m: return -1
        # for i in range(0, n-m+1):
        #     if haystack[i:i+m] == needle:
        #         return i
        # return -1
        # ----------
        # Rabin Karp
        # ----------
        mod = 10 ** 9 + 7
        d = {char: i for i, char in enumerate(chars)}
        needleVal = 0
        for char in needle:
            needleVal = ((needleVal * 26) % mod + d[char]) % mod
        
        substrVal = 0
        for char in haystack[:m]:
            substrVal = ((substrVal * 26) % mod + d[char]) % mod
        if substrVal == needleVal:
            return 0
        
        for i in range(m, n):
            pos = (26 ** (m-1)) % mod
            substrVal = substrVal - (d[haystack[i-m]] * pos) % mod
            substrVal = ((substrVal * 26) % mod + d[haystack[i]]) % mod
            if substrVal == needleVal:
                return i - m + 1
        
        return -1
