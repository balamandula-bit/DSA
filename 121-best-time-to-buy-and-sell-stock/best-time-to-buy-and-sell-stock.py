class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_stock = prices[0]
        max_prof = 0
        for sell_stock in prices:
            if sell_stock < buy_stock:
                buy_stock = sell_stock
            max_prof = max(max_prof, sell_stock - buy_stock)
        
        return max_prof
