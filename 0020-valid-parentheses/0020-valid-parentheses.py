class Solution:
    def isValid(self, s: str) -> bool:
        ob=["(","[","{"]
        cb=[")","]","}"]
        stack=[]
        for i in s:
            if i in ob:
                stack.append(i)
            elif i in cb:
                pos=cb.index(i)
                if(len(stack)>0 and stack[-1]==ob[pos]):
                    stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
        else:
            return False
