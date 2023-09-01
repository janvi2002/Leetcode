class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        if n<=2:
            return 0
#         for kepping track of max height from left side and right side for each bar
        left=[0]*n
        right=[0]*n
        
#         for left
        left[0]=arr[0]
        for i in range(1,n):
            left[i]=max(left[i-1],arr[i])
#         for right
        right[-1]=arr[-1]
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],arr[i])
            
#         using the formula => min(left wall,right wall)-height of current wall = water filled
        water=0
        for i in range(n):
            water+=min(left[i],right[i])-arr[i]
        
        return water
            
        