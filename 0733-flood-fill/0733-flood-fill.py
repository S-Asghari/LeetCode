from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        sColor = image[sr][sc]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        q.append((sr, sc))
        visited = set()
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                image[r][c] = color
                visited.add((r, c))
                for i, j in directions:
                    nr, nc = r+i, c+j
                    if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == sColor and (nr, nc) not in visited:
                        q.append((nr, nc))

        return image