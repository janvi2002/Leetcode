class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind=2
        for i in range(2,len(nums)):
#             if this is true means it is duplicate value nd ind pointed to it 
# now we have to find non duplicate element and place that value in this duplicate place
            if nums[i]==nums[ind-2]:
                continue
            else:
#                 here wehnever we found that value we simply put the value or increment the ind
                nums[ind]=nums[i]
                ind+=1
        return ind
                