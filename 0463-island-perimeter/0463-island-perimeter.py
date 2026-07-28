class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        lands = set()
        commonEdges = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    lands.add((i, j))
                    if i > 0 and (i-1, j) in lands:
                        commonEdges += 1
                    if j > 0 and (i, j-1) in lands:
                        commonEdges += 1
        
        # print(lands)
        # print(edges)
        return len(lands)*4 - commonEdges*2 