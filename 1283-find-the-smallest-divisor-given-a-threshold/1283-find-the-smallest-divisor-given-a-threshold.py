import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def possible(arr,t,divisor):
            sm=0
            for i in arr:
                sm+=math.ceil(i/divisor)
            if sm<=t:
                return True
            return False
        
        ans=0
        left=1
        right=max(nums)
        while left<=right:
            mid=(left+right)//2
            if possible(nums,threshold,mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
