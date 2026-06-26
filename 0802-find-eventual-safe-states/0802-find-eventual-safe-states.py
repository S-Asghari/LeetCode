class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        safe = {}

        def DFS(node):
            safe[node] = False
            for adj in graph[node]:
                if adj in safe and safe[adj]:
                    continue
                elif adj in safe and not safe[adj]:
                    return False
                if not DFS(adj):
                    return False
            safe[node] = True
            return True

        for node in range(len(graph)):
            if node in safe:
                continue
            DFS(node)
        
        result = [node for node in safe if safe[node] is True]
        result.sort()
        return result