class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        l, r = 0, 1
        best_price = 0
        while r < len(prices):
            profit = prices[r]-prices[l]
            best_price = max(best_price, profit)
            if profit >= 0:
                r += 1
            else:
                l = r
                r = r+1
        
        return best_price

