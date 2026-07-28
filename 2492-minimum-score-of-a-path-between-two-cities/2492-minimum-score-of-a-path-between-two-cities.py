from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))
        
        visited = set()
        score = float('inf')

        def DFS(node):
            nonlocal score
            visited.add(node)
            # print(f"node: {node}")
            # print(f"visited: {visited}")
            # print(f"score: {score}\n")
                        
            for nei, d in adj[node]:
                score = min(score, d)
                if nei not in visited:
                    DFS(nei)

        DFS(1)
        return score