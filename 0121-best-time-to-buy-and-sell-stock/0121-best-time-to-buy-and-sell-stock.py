class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprice=prices[0]
        for i in prices:
            if i-minprice>maxprofit:
                maxprofit=i-minprice
            if i<minprice:
                minprice=i
        return maxprofit
