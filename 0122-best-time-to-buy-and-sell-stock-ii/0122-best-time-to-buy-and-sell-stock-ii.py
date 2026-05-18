class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 1
        n = len(prices)
        while i < n:
            if prices[i] > prices[i-1]:
                max_profit += (prices[i]-prices[i-1])
            i+=1
        return max_profit  
         