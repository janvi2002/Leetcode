class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        l=-1
        r=-1
        res=0
        for i in intervals:
            if i[0]>=l and i[1]<=r:
                continue
            res+=1
            l=i[0]
            r=i[1]
        return res
#         brute force solution O(n^2)
        # n=len(intervals)
        # c=0
        # for i in range(n):
        #     for j in range(n):
        #         if i!=j and intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
        #             c+=1
        #             break
        # return n-c
#     otpimizing using sorting O(nlogn)

    
    

    
    