class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l = 0
        res = 0

        for r in range(1, len(intervals)):
            if intervals[r][0] < intervals[l][1]: # There's an overlap
                res += 1
                if intervals[l][1] >= intervals[r][1]:
                    l = r
            else:
                l = r

        return res