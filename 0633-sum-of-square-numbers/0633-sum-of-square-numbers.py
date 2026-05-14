import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = math.floor(math.sqrt(c))
        while end >= start:
            sumOfSquares = start ** 2 + end ** 2
            if sumOfSquares == c:
                return True
            elif sumOfSquares > c:
                end -= 1
            else:
                start += 1
        return False