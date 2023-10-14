class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
# initution - try to remove peak element and coz mainitng ascending order
        stack=list()
        for i in num:
#        remove element untill its a peak element
            while stack and stack[-1]>i and k:
                stack.pop()
                k-=1
# no leadeing zero allowed so we skip zero
            if stack or i!='0':
                stack.append(i)

#             stil if the k are not vanished
        while stack and k:
            stack.pop()
            k-=1
        
        if k: 
            stack = stack[0:-k]
        
        return ''.join(stack) or '0'
            
            
                