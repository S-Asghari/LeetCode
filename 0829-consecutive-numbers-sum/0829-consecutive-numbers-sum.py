from math import sqrt, floor

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 1 # There's always an answer for count = 1
        
        for count in range(2, floor(sqrt(2 * n)) + 1):
            firstNum = max(1, n // count - count // 2)
            total = (firstNum - 1) * count + count * (count + 1) / 2
            while total < n:
                firstNum += 1
                total = (firstNum - 1) * count + count * (count + 1) / 2
            if total == n:
                res += 1

        return res