class Solution:
    def isAnagram(self, st: str, ts: str) -> bool:
        #using maps
        dic={}
        for i in st:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        for j in ts:
            if j in dic:
                dic[j]-=1
            else:
                return False

        for v in dic.values():
            if v>0 or v<0:
                return False
        
        return True
                

