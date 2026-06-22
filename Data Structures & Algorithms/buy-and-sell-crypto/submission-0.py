class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 1000000000000000000000000
        max_profit = 0

        for price in prices:
            if price < lowest:
                lowest = price
            if price - lowest > max_profit:
                max_profit = price - lowest
            
        return max_profit


        