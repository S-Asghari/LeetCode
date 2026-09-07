class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        res = []
        l = 0
        for r in range(1, len(sorted_intervals)):
            if sorted_intervals[l][1] >= sorted_intervals[r][0]:
                sorted_intervals[l][1] = max(sorted_intervals[l][1], sorted_intervals[r][1]) 
            else:
                res.append(sorted_intervals[l])
                l = r
        res.append(sorted_intervals[l])
        return res