class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_stock = prices[0]
        profit = float("-inf")

        for price in prices:

            if buy_stock > price:
                buy_stock = price
            
            curr_prof = price - buy_stock 
            profit = max(profit, curr_prof)
        
        return profit
