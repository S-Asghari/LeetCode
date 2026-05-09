class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        n = len(prices)
        for i in range(0, n):
            found = False
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    found = True
                    result.append(prices[i] - prices[j])
                    break
            if not found:
                result.append(prices[i])

        return result