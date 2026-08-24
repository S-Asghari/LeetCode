class Solution:
    # def findSmallest(self, num):
    #     dIdx = 0
    #     dMin = 10
    #     for i, c in enumerate(num):
    #         if int(c) < dMin:
    #             dMin, dIdx = int(c), i
    #     return str(dMin), dIdx

    def removeKdigits(self, num: str, k: int) -> str:
        # The remaining number would have n - k digits.
        # n = len(num)
        # l = n - k
        
        # res = ""
        
        # i = 0
        # while i < l and k > 0:
        #     d, d_i = self.findSmallest(num[0: k + 1])
        #     res += d
        #     num = num[d_i+1:]
        #     k -= d_i
        #     i += 1
        
        # if i < l:
        #     res += num

        
        # leading_zero = 0
        # while leading_zero < len(res) and res[leading_zero] == '0':
        #     leading_zero += 1

        # return res[leading_zero:] if res[leading_zero:] else "0"
        # -------------------
        # TIME LIMIT EXCEEDED
        # -------------------
        n = len(num)
        stack = []
        for i in range(n):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        res = "".join(stack)
        
        leading_zero = 0
        while leading_zero < len(res) and res[leading_zero] == '0':
            leading_zero += 1

        return res[leading_zero:] if res[leading_zero:] else "0"