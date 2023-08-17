class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        ans=0
        count=0
        while count!=k:
            if i not in arr:
                ans=i
                count+=1
            i+=1
        return ans
                
        