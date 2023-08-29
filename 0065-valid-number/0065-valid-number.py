class Solution:
    def isNumber(self, s: str) -> bool:
        digitseen,eseen,dotseen=False,False,False
        count=0
        n=len(s)
        for i in range(n):
            char=s[i]
#             checking digits
            if char.isdigit():
                digitseen=True
            
#             checking plus minus condition
            elif char=="+" or char=="-":
#         if it occur 2 times means invalid
                if count==2:
                    return False
#         if plus or minus appear after e and index is also greater than 1 means its invalid
                if i>0 and s[i-1]!='e' and s[i-1]!='E':
                    return False
#         if it come at last index also invalid
                if i==n-1:
                    return False
#         else we have to increment the count
                count+=1
    
#    checking for dot  
            elif char==".":
#         if we seen E before or dot before means invalid
                if eseen or dotseen:
                    return False
#         if it is on last index and till now no digit is seen also invalid
                if i==n-1 and not digitseen:
                    return False
#         else make dotseen true
                dotseen=True
    
#     last check e or E
            elif char=="e" or char=="E":
#         if already we see e or till now no digit is seen or if it found on last index its invalid
                if eseen or not digitseen or i==n-1:
                    return False
#         else make them true
                eseen=True
    
#     if the char goes in else part means its not valid number
            else:
                return False
        return True
        