class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minp=prices[0]
        maxp=0
        for price in prices:
            if price < minp:
                minp=price
            profit=price-minp
            if maxp<profit:
                maxp=profit
        return maxp

    