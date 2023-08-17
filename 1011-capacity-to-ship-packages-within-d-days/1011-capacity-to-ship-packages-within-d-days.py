class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def noOfDays(capacity,arr):
#             at day 1 ship loaded with 0 items
            day=1
            load=0
            for i in arr:
#                 at this point if loading capacity exceed the value increse the day and also make load=last container to contiue further packages
                if load+i>capacity: 
                    day+=1
                    load=i
                else:
                    load+=i
            return day
        
#as we idenify the range we simply pass hypothetical capacites and keep checking if the no of days is less than or equal 
        ans=0
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=(left+right)//2
            temp=noOfDays(mid,weights)
            if temp<=days:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
        