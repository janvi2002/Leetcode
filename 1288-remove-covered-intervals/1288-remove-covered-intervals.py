class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         brute force solution
        n=len(intervals)
        c=0
        for i in range(n):
            for j in range(n):
                if i!=j and intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                    c+=1
                    break
        return n-c