from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
        
        answer = set([i for i in range(n)])

        def recurse(node):
            if (node not in answer) or (node not in adj):
                return
            for nei in adj[node]:
                recurse(nei)
                answer.discard(nei)
        
        for node in range(n):
            recurse(node) 

        return list(answer)