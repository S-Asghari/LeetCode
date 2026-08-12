class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        y = 0
        while x:
            r = x % 10
            x = x // 10
            if y > INT_MAX // 10 or (y == INT_MAX // 10 and r > 7):
                return 0
            y = y * 10 + r
        
        return sign * y
