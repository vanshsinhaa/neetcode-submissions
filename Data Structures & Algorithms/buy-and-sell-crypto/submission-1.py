class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        lowest_price = 1000000
        # max profit 
        max_profit = 0


        for price in prices:

            # we need to update the lowest 
            if price < lowest_price:
                lowest_price = price

            # max profit = price - min_price 

            if price - lowest_price > max_profit:
                max_profit = price - lowest_price

        return max_profit        