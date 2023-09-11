class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        i=0
        j=1
        k=len(piles)-1
        ans=0
        while i<len(piles)-2 and j<k:
            ans+=piles[j]
            i+=2
            j+=2
            k-=1
        return ans
            
            