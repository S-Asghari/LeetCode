class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            exchanged = numBottles // numExchange
            res += exchanged
            numBottles -= (numExchange - 1) * exchanged
        return res