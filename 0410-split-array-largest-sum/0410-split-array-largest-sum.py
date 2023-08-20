class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possibleArr(nums,split):
            noOfArr=1
            size=0
            for i in nums:
                if i+size > split:
                    noOfArr+=1
                    size=i
                else:
                    size+=i
            return noOfArr
        left=max(nums)
        right=sum(nums)
        while left<=right:
            mid=(left+right)//2
            arr=possibleArr(nums,mid)
            if arr > k:
                left=mid+1
            else:
                right=mid-1
        return left