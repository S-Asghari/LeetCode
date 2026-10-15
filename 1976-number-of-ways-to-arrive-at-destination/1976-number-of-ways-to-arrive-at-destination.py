from collections import defaultdict
import heapq

MOD = 10**9 + 7

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))

        dist = {v: float('inf') for v in range(n)}
        dist[0] = 0
        ways = {v: 0 for v in range(n)}
        ways[0] = 1
        
        q = [(0, 0)] # (dist of node 0 to node i, node i)

        while q:
            cur_d, cur_node = heapq.heappop(q)
            
            if cur_d > dist[cur_node]: continue

            for nei, t in adj[cur_node]:
                new_d = cur_d + t
                if new_d < dist[nei]:
                    dist[nei] = new_d
                    ways[nei] = ways[cur_node]
                    heapq.heappush(q, (new_d, nei))
                elif new_d == dist[nei]:
                    ways[nei] = (ways[nei] + ways[cur_node]) % MOD
        
        return ways[n-1]
