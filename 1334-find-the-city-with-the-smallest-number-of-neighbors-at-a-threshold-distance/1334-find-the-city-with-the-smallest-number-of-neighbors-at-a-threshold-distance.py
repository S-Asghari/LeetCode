from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf') for j in range(n)] for i in range(n)]
        closeNeighbors = defaultdict(set)
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j: continue
                    dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k] + dist[k][j])
                    if dist[i][j] <= distanceThreshold:
                        closeNeighbors[i].add(j)
                        closeNeighbors[j].add(i)
        
        # print(f"{dist}\n{closeNeighbors}")
        
        desiredCity = -1
        minNeighbors = n
        for city in range(n):
            if city not in closeNeighbors:
                # print(f"City {city} has no close neihbors")
                desiredCity = city
                minNeighbors = 0
            else:
                # print(f"City {city} has {len(closeNeighbors[city])} close neighbors")
                if len(closeNeighbors[city]) <= minNeighbors:
                    minNeighbors = len(closeNeighbors[city])
                    desiredCity = city
        
        return desiredCity