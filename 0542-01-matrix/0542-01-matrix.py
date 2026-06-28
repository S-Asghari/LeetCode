from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        visited = set()
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n 

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        dist = 0

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if mat[i][j] == 1:
                    res[i][j] = dist
                for di, dj in direction:
                    curI, curJ = i+di, j+dj
                    if isValid(curI, curJ) and (curI, curJ) not in visited:
                        queue.append((curI, curJ))
                        visited.add((curI, curJ))
            dist += 1

        return res