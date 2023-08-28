class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
#         prefix array for traveling time
        prefix=[travel[0]]*len(travel)
        for i in range(1,len(travel)):
            prefix[i]=prefix[i-1]+travel[i]
        ans=0
        paper=0
        metal=0
        glass=0
        for i in range(len(garbage)):
            x=len(garbage[i])
            for j in garbage[i]:   #for checking each element of string
                if j=="G":
                    glass=i   #the last index number where it found
                if j=="P":
                    paper=i
                if j=="M":
                    metal=i
            ans+=x    #picking time as all garbage collection takes 1 minute so we simply add the length
            
        #now adding the travel time for >=1 garbage , the summation of array till the index where it found last 
        if paper>=1:
            ans+=prefix[paper-1]
        if metal>=1:
            ans+=prefix[metal-1]
        if glass>=1:
            ans+=prefix[glass-1]
        return ans
            