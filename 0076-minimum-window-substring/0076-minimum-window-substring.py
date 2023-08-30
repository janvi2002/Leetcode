class Solution:
    def minWindow(self, s: str, t: str) -> str:
#         for storing frequency of t
        map1={}
        for i in t:
            map1[i]=map1.get(i,0)+1
        
        dcount=len(t)   #desired count
        left,right=-1,-1
        pcount=0   #present count
        map2={}  #for storing string s frqeuncy to check how many characters are matched
        ans=""
        while True:
            flag1,flag2=False,False
#             if present count < desired count
            while left<len(s)-1 and pcount<dcount:
#         firstly we put first char into map2
                left+=1
                map2[s[left]]=map2.get(s[left],0)+1
                
#         now checking if the item we recently insert in the map having frequency less or equal so incresent present count
#         if map1 doesnt have item it will handle by .get method
                if map2[s[left]] <= map1.get(s[left],0):
                    pcount+=1
                
                flag1=True
            
#             time to collect ans and shrink the pointer to get more minimum length ans
            while right<left and pcount==dcount:
                temp=s[right+1:left+1]
                if len(ans)==0 or len(temp)<len(ans):
                    ans=temp
                
#                 after saving answer if simply decrease the count
                right+=1
                map2[s[right]]=map2[s[right]]-1
#                 now check if the due to decreased count it loss the desire count so 
                if map2[s[right]] < map1.get(s[right],0):
                    pcount-=1
                    
                flag2=True
            
            if flag1==False and flag2==False:
                break
        return ans
                
                
                
        