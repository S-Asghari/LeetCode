from math import ceil
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        n = len(s)
        numCols = ceil(n / numRows) * numRows
        matrix = [['' for _ in range(numCols)] for _ in range(numRows)]
        i, j = 0, 0
        sign = -1
        for c in s:
            matrix[i][j] = c
            j += 1
            if i == 0 or i == numRows - 1:
                sign *= -1
            i += sign
        
        newS = ''
        for row in matrix:
            newS += ''.join(row)
        return newS