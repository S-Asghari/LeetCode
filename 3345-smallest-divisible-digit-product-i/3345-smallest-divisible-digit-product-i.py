class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        p = 1
        num = n
        while num > 0:
            p *= (num % 10)
            num //= 10
        
        while p % t != 0:
            if n % 10 < 9:
                p //= (n % 10)
                p *= ( n % 10 + 1)
                n += 1
            else: # n % 10 = 9
                p = 0
                n += 1
        
        return n