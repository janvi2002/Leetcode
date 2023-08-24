class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        k=0
        while i<=j:
            if nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
                if nums[i]!=val:
                    i+=1
                    k+=1
            else:
                i+=1
                k+=1
        return k
        
        
            