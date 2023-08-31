class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        maxi=0
        for i in nums:
#             that means i is the starting value so we keep count from here ans store length
            if i-1 not in s:
                currval=i+1
                currcount=1
                while currval in s:
                    currcount+=1
                    currval+=1
                maxi=max(maxi,currcount)
        return maxi