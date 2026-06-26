class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        visited = {}
        
        def DFS(i):
            if i in visited:
                return visited[i]
            
            visited[i] = False
            
            if arr[i] == 0:
                visited[i] = True
                return True
            
            if i - arr[i] >= 0 and DFS(i - arr[i]):
                visited[i] = True
                return True
            
            if i + arr[i] < N and DFS(i + arr[i]):
                visited[i] = True
                return True
            
            return False

        return DFS(start)