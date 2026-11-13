class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # NeetCode's solution (Topological Sort)
        res = []
        adj = {c: [] for c in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        visited, cycle = set(), set()

        def DFS(crs):
            if crs in cycle: return False
            if crs in visited: return True

            cycle.add(crs)
            for pre in adj[crs]:
                if not DFS(pre): 
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True


        for c in range(numCourses):
            if not DFS(c):
                return []
        return res