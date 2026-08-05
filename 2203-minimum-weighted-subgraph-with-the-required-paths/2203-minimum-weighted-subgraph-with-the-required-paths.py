from collections import defaultdict
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        adj = defaultdict(list)
        reverse_adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            reverse_adj[v].append((u, w))

        def dijkstra(src, adj):
            dist = {node: (float('inf'), None) for node in range(n)}
            dist[src] = (0, None)
            q = [(0, src)]
            visited = set()

            while q:
                curDist, curNode = heapq.heappop(q)
                if curNode in visited: continue
                visited.add(curNode)

                for nextNode, w in adj[curNode]:
                    if nextNode not in visited:
                        newDist = curDist + w
                        if newDist < dist[nextNode][0]:
                            dist[nextNode] = (newDist, curNode)
                            heapq.heappush(q, (newDist, nextNode))

            return dist

        dist1 = dijkstra(src1, adj)
        dist2 = dijkstra(src2, adj)
        dist3 = dijkstra(dest, reverse_adj)

        minWeight = float('inf')
        for lca in range(n):
            newWeight = dist1[lca][0] + dist2[lca][0] + dist3[lca][0]
            minWeight = min(minWeight, newWeight)
        
        if minWeight < float('inf'):
            return minWeight
        else:
            return -1