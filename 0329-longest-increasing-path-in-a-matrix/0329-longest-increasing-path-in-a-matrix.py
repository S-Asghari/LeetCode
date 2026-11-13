class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        memo: dict[tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            longest = 1

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < rows
                    and 0 <= nj < cols
                    and matrix[ni][nj] > matrix[i][j]
                ):
                    longest = max(longest, 1 + dfs(ni, nj))

            memo[(i, j)] = longest
            return longest

        longest = 0
        for i in range(rows):
            for j in range(cols):
                longest = max(longest, dfs(i, j))

        return longest