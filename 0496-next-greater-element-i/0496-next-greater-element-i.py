class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            f=0
            temp=nums2.index(nums1[i])
            for j in range(temp+1,len(nums2)):
                if nums1[i]<nums2[j]:
                    nums1[i]=nums2[j]
                    f=1
                    break
            if f==0:
                nums1[i]=-1
        return nums1