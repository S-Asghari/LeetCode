from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        adj = defaultdict(list)
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        
        best_solution = 0
        
        def DFS(u, visited, timeLeft):
            nonlocal best_solution
            if timeLeft < 0:
                return

            if u == 0:
                current_value = 0
                for node in visited:
                    current_value += values[node]
                best_solution = max(best_solution, current_value)

            for v, t in adj[u]:
                DFS(v, visited.union(set([v])), timeLeft - t)
                
        
        DFS(0, set([0]), maxTime)
        return best_solution