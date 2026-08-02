from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        visited = set()
        dist = {node: (float('inf'), None) for node in range(1, n+1)}
        dist[k] = (0, None)
        q = [(0, k)]

        while q:
            curDist, curNode = heapq.heappop(q)
            if curNode in visited:
                continue
            visited.add(curNode)
            for nei, w in adj[curNode]:
                newDist = curDist + w
                if dist[nei][0] > newDist:
                    dist[nei] = (newDist, curNode)
                    heapq.heappush(q, (newDist, nei))
            
        if len(visited) < n:
            return -1

        minTime = 0
        for node in dist:
            minTime = max(minTime, dist[node][0])
        return minTime