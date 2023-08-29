class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        ans=float('inf')
        left=sm=0
        for right in range(n):
            sm+=nums[right]
            while sm>=target:
                ans=min(right-left+1,ans)
                sm-=nums[left]
                left+=1
                
        return ans if ans!=float("inf") else 0