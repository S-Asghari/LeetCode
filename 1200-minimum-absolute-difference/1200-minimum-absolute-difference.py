class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 1. Sort arr: n log n
        # 2. Find distance between adjacents: n
        # 3. Find min distance
        n = len(arr)
        arr.sort()
        dif_map = {}
        min_dif = float('inf')
        for i in range(0, n-1):
            dif = arr[i+1] - arr[i]
            if dif in dif_map:
                dif_map[dif].append([arr[i], arr[i+1]])
            else:
                dif_map[dif] = [[arr[i], arr[i+1]]]
                min_dif = min(min_dif, dif)
        
        return dif_map[min_dif]