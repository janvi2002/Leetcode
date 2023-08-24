class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # try:
        #     return haystack.index(needle)
        # except:
        #     return -1
        if haystack==needle:
            return 0
        i=0
        j=len(needle)
        while j<=len(haystack):
            temp=haystack[i:j]
            if temp==needle:
                return i
            i+=1
            j+=1
        return -1
            