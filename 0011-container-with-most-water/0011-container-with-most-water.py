class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max_water=0
#         taking two pointer left end and right end of container
        left=0
        right=n-1
        while left<right:
            left_height=height[left]
            right_height=height[right]
#             using the formula min height for the selected container * width of the container (using index)
            curr_water=min(left_height,right_height)*(right-left)
            max_water=max(max_water,curr_water)
#             we increase the minimum height because as it always gives less water so we check for other height
            if left_height<=right_height:
                left+=1
            if right_height<left_height:
                right-=1
        
        return max_water
        
        
        
