class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        startToIdx = {intervals[i][0]: i for i in range(n)}
        sorted_start = sorted([interval[0] for interval in intervals])
        intervals = sorted(intervals, key = lambda x: x[1])
        # print(f"startToIdx = {startToIdx}")
        # print(f"sorted_start = {sorted_start}")
        # print(f"intervals = {intervals}")
        res = [-1 for i in range(n)]
        p = 0 # pointer
        for interval in intervals:
            while p < n and sorted_start[p] < interval[1]:
                p += 1
            if p < n:
                s = interval[0]
                idx = startToIdx[s]
                right_intrvl_strt = sorted_start[p]
                res[idx] = startToIdx[right_intrvl_strt]
                
        return res