class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2, n+1):
            row = [1 for _ in range(i)]
            for j in range(1, i-1):
                row[j] = res[-1][j-1] + res[-1][j]
            res.append(row)
        return res