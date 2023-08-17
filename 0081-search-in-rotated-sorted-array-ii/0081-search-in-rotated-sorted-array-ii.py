class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            # cox if three of them are equal it is not possible to find sorted part to just shrink iy
            if nums[mid]==nums[left]==nums[right]:
                left+=1
                right-=1
                continue
            
            if nums[mid]>=nums[left]:
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False