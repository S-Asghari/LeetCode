import math

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(seq):
            inverted = ""
            for c in seq:
                if c == '0': inverted += '1'
                else: inverted += '0'
            return inverted

        n = math.ceil(math.log2(k+1))
        s = "0"
        for i in range(2, n+1):
            inverted = invert(s)
            s += '1' + inverted[::-1]
        return s[k-1]