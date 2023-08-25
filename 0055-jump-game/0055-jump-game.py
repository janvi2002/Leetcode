class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
# we try to check reverse of the index number of array + value greater than index 
# if yes then update index with the current index number
            if nums[i]+i>=index:
                index=i
# if it successfully reaches to 0 that means we jump easily else not
        return True if index==0 else False
        