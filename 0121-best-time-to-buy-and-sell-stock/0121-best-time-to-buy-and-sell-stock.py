class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minpro = float("inf")
        maxpro = 0
        n = len(prices)
        for i in range(n):
            minpro = min(minpro, prices[i])
            maxpro = max(maxpro, prices[i] - minpro)

        return maxpro 