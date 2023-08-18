class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        positive = True
        s = s.lstrip()
        if not s:
            return 0
        if s[0] == "-":
            positive = False
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        if not s:
            return 0
        for i in s:
            if i in "0123456789":
                result += i
            else:
                break  
        if not result:
            return 0
       
        if positive:
            return min(int(result), 2**31-1)
        return max(-2**31, -int(result))
        