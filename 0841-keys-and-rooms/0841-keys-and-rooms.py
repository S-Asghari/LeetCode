class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        
        def DFS(node):
            if node in visited:
                return
            visited.add(node)
            for adj in rooms[node]:
                DFS(adj)
            return

        DFS(0)
        if len(visited) < n:
            return False
        return True