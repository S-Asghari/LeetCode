from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ------------
        # DFS Solution
        # ------------
        # m, n = len(grid), len(grid[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # visited = set()
        # count = 0

        # def DFS(i, j):
        #     visited.add((i, j))

        #     for di, dj in directions:
        #         if 0 <= i + di < m and 0 <= j + dj < n and (i+di, j+dj) not in visited:
        #             if grid[i+di][j+dj] == "1":
        #                 DFS(i+di, j+dj)

        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) not in visited and grid[i][j] == "1":
        #             count += 1
        #             DFS(i, j)

        # return count
        
        # ------------
        # BFS Solution
        # ------------
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        islands = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    grid[r][c] = "0" # Mark as visited
                    q = deque([(r, c)])

                    while q:
                        i, j = q.popleft()
                        for di, dj in directions:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                                grid[ni][nj] = "0" # Mark as visited
                                q.append((ni, nj))
        
        return islands