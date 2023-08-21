class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        count=0
        j=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
            else:
                count-=1
                if count==0:
                    ans+=s[j+1:i]
                    j=i+1
        return ans