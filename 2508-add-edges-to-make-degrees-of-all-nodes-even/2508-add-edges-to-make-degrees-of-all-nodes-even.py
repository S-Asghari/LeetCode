from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        odds = []
        for node in adj:
            if len(adj[node]) % 2 == 1:
                odds.append(node)
        
        if len(odds) == 0:
            return True
        
        if len(odds) == 2:
            node1, node2 = odds
            if node2 not in adj[node1]: return True
            for node3 in range(1, n+1):
                if node3 == node1 or node3 == node2: continue
                if (node1 not in adj[node3]) and (node2 not in adj[node3]):
                    return True
            return False
        
        if len(odds) == 4:
            node1, node2, node3, node4 = odds
            if (node2 not in adj[node1]) and (node4 not in adj[node3]): return True
            if (node3 not in adj[node1]) and (node4 not in adj[node2]): return True
            if (node4 not in adj[node1]) and (node3 not in adj[node2]): return True
            return False
        
        if len(odds) > 4:
            return False
