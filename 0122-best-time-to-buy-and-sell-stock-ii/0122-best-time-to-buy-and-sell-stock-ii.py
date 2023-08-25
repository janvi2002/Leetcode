class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        for i in range(1,len(prices)):
#             simply check if ith is greter than i-1 then we can by or sell it and add simple profit to the answer
            if prices[i-1]<prices[i]:
                ans+=prices[i]-prices[i-1]
        return ans
            
            