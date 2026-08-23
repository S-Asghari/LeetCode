class Solution:
    def intToRoman(self, num: int) -> str:
        conversion = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = ""
        p = 3
        while num > 0:
            if num >= 10 ** p:
                d = num // 10 ** p
                if 5 <= d <= 8:
                    res += conversion[5 * 10 ** p]
                    num -= 5 * 10 ** p
                elif 1 <= d <= 3:
                    res += conversion[10 ** p] * d
                    num %= 10 ** p
                    p -= 1
                elif d == 4 or d == 9:
                    res += conversion[10 ** p]
                    num += 10 ** p
                    p += 1
            else:
                p -= 1

        return res