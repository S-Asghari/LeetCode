class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        result = []
        left_i, left_j = sorted_intervals.pop(0)
        while sorted_intervals:
            i, j = sorted_intervals.pop(0)
            if i <= left_j:
                left_j = max(left_j, j)
            else: # i > left_j
                result.append([left_i, left_j])
                left_i, left_j = i, j
        result.append([left_i, left_j])
        return result
