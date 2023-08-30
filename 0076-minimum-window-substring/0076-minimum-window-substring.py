class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map1={}
        for i in t:
            map1[i]=map1.get(i,0)+1
        
        dcount=len(t)
        left,right=-1,-1
        pcount=0
        map2={}
        ans=""
        while True:
            flag1,flag2=False,False
            while left<len(s)-1 and pcount<dcount:
                left+=1
                map2[s[left]]=map2.get(s[left],0)+1
                
                if map2[s[left]] <= map1.get(s[left],0):
                    pcount+=1
                
                flag1=True
            
            while right<left and pcount==dcount:
                temp=s[right+1:left+1]
                if len(ans)==0 or len(temp)<len(ans):
                    ans=temp
                right+=1
                map2[s[right]]=map2[s[right]]-1
                
                if map2[s[right]] < map1.get(s[right],0):
                    pcount-=1
                
                flag2=True
            
            if flag1==False and flag2==False:
                break
        return ans
                
                
                
        