class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l, r = 0, 1
        res = 0

        while r < len(intervals):
            if intervals[r][0] < intervals[l][1]: # There's an overlap
                res += 1
                if intervals[r][1] > intervals[l][1]:
                    r += 1
                else: # intervals[l][1] >= intervals[r][1]
                    l = r
                    r += 1
            else:
                l = r
                r += 1
        return res

        return res