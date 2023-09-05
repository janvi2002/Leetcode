class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1],reverse=True)
        ans=0
        for i in range(len(boxTypes)):
            mini=min(truckSize,boxTypes[i][0])
            ans+=mini*boxTypes[i][1]
            truckSize-=mini
            if truckSize==0:
                break
        return ans
