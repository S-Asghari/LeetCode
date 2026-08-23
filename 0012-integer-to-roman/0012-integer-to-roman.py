class Solution:
    def intToRoman(self, num: int) -> str:
        conversion = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = ""
        p = 3
        while num > 0:
            print(res)
            print(num)
            if num >= 1000:
                d = num // 1000
                res += conversion[1000] * d
                num %= 1000
            
            elif num >= 100:
                d = num // 100
                if 5 <= d <= 8:
                    res += conversion[500]
                    num -= 500
                elif 1 <= d <= 3:
                    res += conversion[100] * d
                    num %= 100
                elif d == 4 or d == 9:
                    res += conversion[100]
                    num += 100
            
            elif num >= 10:
                d = num // 10
                if 5 <= d <= 8:
                    res += conversion[50]
                    num -= 50
                elif 1 <= d <= 3:
                    res += conversion[10] * d
                    num %= 10
                elif d == 4 or d == 9:
                    res += conversion[10]
                    num += 10
            
            elif num >= 1:
                d = num
                if 5 <= d <= 8:
                    res += conversion[5]
                    num -= 5
                elif 1 <= d <= 3:
                    res += conversion[1] * d
                    num = 0
                elif d == 4 or d == 9:
                    res += conversion[1]
                    num += 1

        return res