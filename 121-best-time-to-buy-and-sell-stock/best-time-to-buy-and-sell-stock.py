class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        curr_prof = max_prof = 0
        buy = prices[0]
        for i in range(n):
            buy = min(buy, prices[i])
            curr_prof = prices[i] - buy
            max_prof = max(curr_prof, max_prof)
        
        return max_prof