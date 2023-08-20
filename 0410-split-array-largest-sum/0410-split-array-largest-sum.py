class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possibleArr(nums,split):
#             initially there is only 1 array  with size 0
            noOfArr=1
            size=0
            for i in nums:
#                 here we simply add the elements till the split value exceed 
                if i+size > split:
                    noOfArr+=1
                    size=i
                else:
                    size+=i
#             and return the total no of array we formed with the help of given splitter 
            return noOfArr
#         problem is same to book allocation problem
# here we take left as max number coz the least split we can do is that particular number
        left=max(nums)
#     and max is sum of all nums
        right=sum(nums)
        while left<=right:
            mid=(left+right)//2
            arr=possibleArr(nums,mid)
#             here we check if the no of splitted array is greater than k then we move higher side to give big range to split the array so we get the minimum or equal to k size array
            if arr > k:
                left=mid+1
            else:
                right=mid-1
# at last we print left bcoz we want minimum of maximum 
        return left  