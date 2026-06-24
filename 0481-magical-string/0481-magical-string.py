class Solution:
    def magicalString(self, n: int) -> int:
        def nextVal(v):
            if v == '1': return '2'
            else: return '1'
        
        s = "122"
        nextIdx = 2
        preVal = '2'
        ones = 1

        while n > len(s):
            preVal = nextVal(preVal)
            s += int(s[nextIdx]) * preVal
            if preVal == '1': ones += int(s[nextIdx])
            nextIdx += 1
        
        for i in range(n, len(s)):
            if s[i] == '1':
                ones -= 1
        
        return ones