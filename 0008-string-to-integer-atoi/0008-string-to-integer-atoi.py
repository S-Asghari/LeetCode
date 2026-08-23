from math import floor, ceil

class Solution:
    def myAtoi(self, s: str) -> int:
        maxBound = 2 ** 31 - 1
        minBound = -2 ** 31
        num = ""
        sign = 1
        i = 0
        
        # step 1
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # step 2
        if i < len(s):
            if s[i] == '+':
                i += 1
            elif s[i] == '-':
                sign = -1
                i += 1
        
        # step 3
        while i < len(s) and s[i] == '0':
            i += 1
        
        # step 4
        while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
            num += s[i]
            i += 1
        
        res = 0
        if sign == 1:
            for i in range(len(num)):
                res = res * 10 + int(num[i])
                if (res > floor(maxBound / 10) and i < len(num)-1) or \
                (res == floor(maxBound / 10) and i < len(num)-1 and int(num[i+1]) >= maxBound % 10):
                    res = maxBound
                    break
        else:
            for i in range(len(num)):
                res = res * 10 - int(num[i])
                if (res < ceil(minBound / 10) and i < len(num)-1) or \
                (res == ceil(minBound / 10) and i < len(num)-1 and int(num[i+1]) >= 10 - (minBound % 10)):
                    res = minBound
                    break

        return res