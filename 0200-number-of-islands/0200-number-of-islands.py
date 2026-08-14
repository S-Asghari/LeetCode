class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        count = 0

        def DFS(i, j):
            visited.add((i, j))

            for di, dj in directions:
                if 0 <= i + di < m and 0 <= j + dj < n and (i+di, j+dj) not in visited:
                    if grid[i+di][j+dj] == "1":
                        DFS(i+di, j+dj)

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    count += 1
                    DFS(i, j)

        return count