class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # for i in range(len(arr)-1):
        #     if arr[i]<arr[i+1]:
        #         continue
        #     else:
        #         return i
        
#         via binary search
        l, r = 0, len(arr)-1 
        while l <= r:
            m = (l+r)//2
            if arr[m+1] < arr[m] and arr[m-1] < arr[m]:
                return m
            if arr[m+1] > arr[m]:
                l = m+1
            else:
                r = m