from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])
        height = [[-1 for j in range(col)] for i in range(row)]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = deque()

        def fillSurrounding(i, j):
            updatedCells = []
            for d1, d2 in directions:
                if 0 <= i + d1 < row and 0 <= j + d2 < col and height[i+d1][j+d2] == -1:
                    height[i+d1][j+d2] = height[i][j] + 1
                    updatedCells.append((i+d1, j+d2))
            return updatedCells


        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()
            updatedCells = fillSurrounding(i, j)
            for i2, j2 in updatedCells:
                queue.append((i2, j2))
        
        return height
