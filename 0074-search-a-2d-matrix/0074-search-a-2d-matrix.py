class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        
        s, e = 0, M * N - 1
        while s <= e and s < M * N and e >= 0:
            m = (s + e) // 2
            mi, mj = m // N, m % N

            if matrix[mi][mj] == target:
                return True
            elif matrix[mi][mj] > target:
                e = m - 1
            else:
                s = m + 1
        
        return False