from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        
        def DFS(node):
            if node == destination:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if DFS(nei):
                        return True
            return False
        
        return DFS(source)
