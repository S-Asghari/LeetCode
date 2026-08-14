class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        res = float('inf')
        
        # Plan A: Start by a land ride
        # 1. Find earliest land ride finish time 
        lf = float('inf')
        for i in range(n):
            lf = min(lf, landStartTime[i] + landDuration[i])
        # 2. Check all water rides
        for j in range(m):
            if waterStartTime[j] <= lf:
                res = min(res, lf + waterDuration[j])
            else:
                res = min(res, waterStartTime[j] + waterDuration[j])
        
        # Plan B: Start by a water ride
        # 1. Find earliest water ride finish time
        wf = float('inf')
        for j in range(m):
            wf = min(wf, waterStartTime[j] + waterDuration[j])
        # 2. Check all land rides
        for i in range(n):
            if landStartTime[i] <= wf:
                res = min(res, wf + landDuration[i])
            else:
                res = min(res, landStartTime[i] + landDuration[i])

        return res