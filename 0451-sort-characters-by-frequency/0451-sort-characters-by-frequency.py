class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        
        x=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for i in x:
            ans+=i[0]*i[1]
        return ans