class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        s=s.rstrip()
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                c+=1
            else:
                break
        return c