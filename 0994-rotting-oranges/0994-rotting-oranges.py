from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        fresh = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i, j))
                elif grid[i][j] == 1: fresh.add((i, j))
        minutes = 0
        while q:
            if not fresh:
                return minutes
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) in fresh:
                        grid[i+di][j+dj] = 2
                        fresh.discard(((i+di, j+dj)))
                        q.append((i+di, j+dj))
            minutes += 1
        if not fresh:
            return minutes
        else:
            return -1