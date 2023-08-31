class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        currsum=0
        for i in range(len(nums)):
            currsum+=nums[i]
            if currsum>sum:
                sum=currsum
            if currsum<0:
                currsum=0
        return sum
            
    