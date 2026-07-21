class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph)
        def BFS(source, path):
            if source == n - 1:
                paths.append(path.copy())
            for nei in graph[source]:
                path.append(nei)
                BFS(nei, path)
                path.pop()
        
        BFS(0, [0])
        return paths