class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        # NeetCode's solution
        
        m = len(matrix)
        n = len(matrix[0])

        cache = {}
        
        def DFS(row, col):
            if row == m or col == n or matrix[row][col] == 0:
                return 0
            
            if (row, col) not in cache: 
                cache[(row, col)] = 1 + min(
                    DFS(row + 1, col),
                    DFS(row, col + 1),
                    DFS(row + 1, col + 1)
                )
            return cache[(row, col)]
    
        res = 0

        for i in range(m):
            for j in range(n):
                res += DFS(i, j)

        return res