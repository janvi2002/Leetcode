import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # # brute force solution
        # # taking the number from starting 
        # for i in range(1,max(piles)+1):
        #     sm=0
        #     # now here check if koko eat 3banana in 1 to max piles hrs. and we keep the sum of ceil values
        #     for j in piles:
        #         sm+=math.ceil(j/i)
        #         # at any point sm is greater than h break coz it not possible
        #         if sm>h:
        #             break
        #     else:
        #         # after succesful for loop ans would be i
        #         return i

        # binary search optimization for deciding hours range
        def koko(value,arr):
            sm=0
            for i in arr:
                sm+=math.ceil(i/value)
            return sm

        left=1
        right=max(piles)
        ans=1
        while left<=right:
            mid=(left+right)//2
            temp=koko(mid,piles)
            if temp<=h:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans