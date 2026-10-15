class Solution:
    def trunc(self, x):
        factor = 10 ** 5
        x *= factor
        x = math.trunc(x)
        x /= factor
        return x

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = 0
        var_hash = {}

        for a, b in equations:
            if a not in var_hash:
                var_hash[a] = n
                n += 1
            if b not in var_hash:
                var_hash[b] = n
                n += 1

        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dist[i][i] = 1

        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]
            a_idx, b_idx = var_hash[a], var_hash[b]

            dist[a_idx][b_idx] = v
            dist[b_idx][a_idx] = 1/v

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] == float('inf') and \
                    dist[i][k] < float('inf') and \
                    dist[k][j] < float('inf'):
                        dist[i][j] = dist[i][k] * dist[k][j]
        
        res = []
        for a, b in queries:
            if (a not in var_hash) or (b not in var_hash):
                res.append(-1.0)
                continue

            a_idx, b_idx = var_hash[a], var_hash[b]
            if dist[a_idx][b_idx] == float('inf'):
                res.append(-1.0)
            else:
                res.append(self.trunc(dist[a_idx][b_idx]))
        
        return res