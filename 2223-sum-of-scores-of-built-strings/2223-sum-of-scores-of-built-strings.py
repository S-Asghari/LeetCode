# from collections import defaultdict

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        # total = n

        # prefix = 0
        # base = 29
        # mod = 10 ** 9 + 7
        # encoded_prefixes = defaultdict(int)
        # for i in range(n):
        #     char = ord(s[i]) - ord('a') + 1
        #     prefix = ((prefix * base) % mod + char) % mod
        #     encoded_prefixes[i+1] = prefix
        
        # for i in range(1, n):
        #     encoded_substr = 0
        #     j = i
        #     while j < n:
        #         char = ord(s[j]) - ord('a') + 1
        #         encoded_substr = ((encoded_substr * base) % mod + char) % mod
        #         if encoded_substr == encoded_prefixes[j-i+1]:
        #             j += 1
        #             total += 1
        #         else:
        #             break
        # return total
        # -------------------
        # TIME LIMIT EXCEEDED
        # -------------------

        # memo = [[-1 for r in range(n)] for l in range(n)]
        # total = 0
        
        # def recursive(l, r):
        #     if l == r and 0 <= l < n:
        #         char = ord(s[r]) - ord('a') + 1
        #         memo[l][r] = char
        #         return memo[l][r]

        #     if r < l or l < 0 or r < 0: return 0
            
        #     if memo[r][r] == -1: recursive(r, r)
        #     if memo[l][r-1] == -1: recursive(l, r-1)
        #     if memo[l][r-1] != memo[0][r-l-1] or memo[r][r] != memo[r-l][r-l]:
        #         memo[l][r] = 0
        #     else:
        #         memo[l][r] = memo[l][r-1] * 29 + memo[r][r]
           
        #     return memo[l][r]
        
        
        # for l in range(0, n):
        #     recursive(l, n-1)
        
        # for l in range(0, n):
        #     for r in range(n-1, l-1, -1):
        #         if memo[l][r] > 0:
        #             if l == r and memo[r][r] != memo[0][0]:
        #                 break
        #             total += r-l+1
        #             break
        
        # return total
        # -------------------
        # TIME LIMIT EXCEEDED
        # -------------------
        
        z = [0 for _ in range(n)]
        z[0] = n
        
        l, r = 0, 0 # current Z-box: [l, r)
        for i in range(1, n):
            if i < r:
                z[i] = min(z[i-l], r-i)
            while i + z[i] < n and s[i + z[i]] == s[z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l = i
                r = i + z[i]

        return sum(z)