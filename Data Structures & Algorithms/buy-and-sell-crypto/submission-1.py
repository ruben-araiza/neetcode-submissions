class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best_profit = 0
        l, r = 0, 1
        while r < n:
            if prices[r] > prices[l]: # we can make profit
                profit = prices[r] - prices[l]
                best_profit = max(best_profit, profit)
            else:
                l = r
            r += 1
        return best_profit

