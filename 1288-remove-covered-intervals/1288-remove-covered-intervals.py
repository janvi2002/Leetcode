class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#     otpimizing using sorting O(nlogn)
        intervals.sort(key=lambda x:(x[0],-x[1]))   #here we do ascending sorting for first element and descending sorting on second to prevent error
        left=-1
        right=-1
        res=0
        for i in intervals:
            if i[0]>=left and i[1]<=right:
                continue
            res+=1
            left=i[0]
            right=i[1]
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


    
    

    
    