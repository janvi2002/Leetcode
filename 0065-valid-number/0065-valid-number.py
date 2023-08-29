class Solution:
    def isNumber(self, s: str) -> bool:
        digitseen,eseen,dotseen=False,False,False
        count=0
        n=len(s)
        for i in range(n):
            char=s[i]
            
            if char.isdigit():
                digitseen=True
            
            elif char=="+" or char=="-":
                if count==2:
                    return False
                if i>0 and s[i-1]!='e' and s[i-1]!='E':
                    return False
                if i==n-1:
                    return False
                count+=1
            elif char==".":
                if eseen or dotseen:
                    return False
                if i==n-1 and not digitseen:
                    return False
                dotseen=True
            elif char=="e" or char=="E":
                if eseen or not digitseen or i==n-1:
                    return False
                eseen=True
            else:
                return False
        return True
        