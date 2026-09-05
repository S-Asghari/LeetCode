from math import floor, ceil, log
class Solution:
    def minOperations(self, n: int) -> int:
        # memo = [float('inf')] * (n+1)
        
        # for i in range(0, floor(log(n, 2))+1):
        #     memo[2 ** i] = 1
        
        # for i in range(1, n+1):
        #     if memo[i] < float('inf'): continue
        #     for j in range(1, i // 2 + 1):
        #         memo[i] = min(memo[i], memo[j] + memo[i-j])
        
        # return memo[n]

        def recursive(n):
            lg = log(n, 2)
            if floor(lg) == ceil(lg):
                return 1
            margin1 = 2 ** floor(lg)
            margin2 = 2 ** ceil(lg)
            
            return min(
                recursive(n - margin1),
                recursive(margin2 - n)
            ) + 1
        
        return recursive(n)
