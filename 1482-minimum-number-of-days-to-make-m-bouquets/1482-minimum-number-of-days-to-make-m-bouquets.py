class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Brute force
        # if m*k>len(bloomDay):
        #     return -1
        # def possible(bloomDay,day,m,k):
        #     flower=0
        #     count=0
        #     for j in bloomDay:
        #         if j<=i:
        #             count+=1
        #         else:
        #             flower+=count//k
        #             count=0
        #     # for the last adjancent 
        #     flower+=count//k
        #     if flower>=m:
        #         return True
        #     return False
        
        # days=max(bloomDay)
        # for i in range(min(bloomDay),max(bloomDay)+1):
        #     if possible(bloomDay,i,m,k):
        #         days=min(days,i)
        # return days

        # optimizid by binary search
        if m*k>len(bloomDay):
            return -1
        def possible(bloomDay,day,m,k):
            flower=0
            count=0
            for j in bloomDay:
                if j<=day:
                    count+=1
                else:
                    flower+=count//k
                    count=0
            # for the last adjancent 
            flower+=count//k
            if flower>=m:
                return True
            return False
        
        days=0
        left=min(bloomDay)
        right=max(bloomDay)
        while left<=right:
            mid=(left+right)//2
            if possible(bloomDay,mid,m,k):
                days=mid
                right=mid-1
            else:
                left=mid+1
        return days
