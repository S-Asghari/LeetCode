class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        globalSum = []
        c = 0
        while a or b or c:
            curSum = 0
            if a: curSum += int(a.pop())
            if b: curSum += int(b.pop())
            curSum += c

            c = curSum // 2
            curSum %= 2

            globalSum.append(curSum)

        res = ""
        for i in range(len(globalSum)-1, -1, -1):
            res += str(globalSum[i])
        return res