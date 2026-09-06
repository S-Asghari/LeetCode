from typing import List
from collections import deque

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        dirEdges = [set() for _ in range(n)]
        undirEdges = [set() for _ in range(n)]
        for u, v in edges:
            dirEdges[u].add(v)
            undirEdges[u].add(v)
            undirEdges[v].add(u)

        def edgeCost(parent, child):
            return 0 if child in dirEdges[parent] else 1

        parent = [-1] * n
        order = [0]
        visited = [False] * n
        visited[0] = True
        q = deque([0])
        while q:
            u = q.popleft()
            for nei in undirEdges[u]:
                if not visited[nei]:
                    visited[nei] = True
                    parent[nei] = u
                    order.append(nei)
                    q.append(nei)

        cost = [0] * n
        for u in order[1:]:
            cost[u] = edgeCost(parent[u], u)

        answer = [0] * n
        answer[0] = sum(cost[u] for u in order[1:])

        for u in order[1:]:
            p = parent[u]
            # remove old cost of p -> u & add new cost of u -> p
            answer[u] = answer[p] - cost[u] + (1 - cost[u])

        return answer