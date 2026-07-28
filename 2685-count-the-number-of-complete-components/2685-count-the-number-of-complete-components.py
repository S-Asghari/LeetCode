from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        components = []
        visited = set()
        
        def DFS(node, component):
            visited.add(node)
            component.add(node)
            for nei in adj[node]:
                if nei not in component:
                    DFS(nei, component)
            return component

        for node in range(n):
            if node not in visited:
                newComponent = DFS(node, set())
                components.append(newComponent)
        
        completeComponents = 0
        for c in components:
            isComplete = True
            V = len(c)
            for node in c:
                if len(adj[node]) < V - 1:
                    isComplete = False
                    break
            if isComplete:
                completeComponents += 1

        return completeComponents