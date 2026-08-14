class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle1 = (hour / 12) * 360 + (minutes / 60) * 30
        angle2 = (minutes / 60) * 360
        res = abs(angle1 - angle2)
        if res > 180:
            res = 360 - res
        return res