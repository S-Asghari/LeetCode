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

        # ---------------
        # Greedy Solution
        # ---------------
        # def recursive(n):
        #     lg = log(n, 2)
        #     if floor(lg) == ceil(lg):
        #         return 1
        #     margin1 = 2 ** floor(lg)
        #     margin2 = 2 ** ceil(lg)
            
        #     return min(
        #         recursive(n - margin1),
        #         recursive(margin2 - n)
        #     ) + 1
        
        # return recursive(n)
        # -------------------------
        # Bit Manipulation Solution
        # -------------------------
        count = 0
        while n:
            if n & 1:
                count += 1
                if n & 2:      # next bit is also 1 -> round up
                    n += 1
                else:
                    n -= 1
            n >>= 1
        return count
