from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # NeetCode's Solution
        N = len(grid)
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def invalid(r, c):
            return r < 0 or r == N or c < 0 or c == N

        def DFS(r, c):
            if invalid(r, c) or grid[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in direction:
                DFS(r+dr, c+dc)

        def BFS():
            result, q = 0, deque(visited)

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direction:
                        curR, curC = r+dr, c+dc
                        if invalid(curR, curC) or (curR, curC) in visited:
                            continue
                        if grid[curR][curC] == 1:
                            return result
                        else:
                            q.append((curR, curC))
                            visited.add((curR, curC))
                result += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    DFS(r, c)
                    return BFS()