class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = 0, 0
        i = 0
        while i < len(prices):
            if prices[i] >= prices[sell]:
                sell = i
                profit = max(profit, prices[sell] - prices[buy])
            elif prices[i] < prices[buy]:
                buy = i
                sell = i
            i += 1
        return profit