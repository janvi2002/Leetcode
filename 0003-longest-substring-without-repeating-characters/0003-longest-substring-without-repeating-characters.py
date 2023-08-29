class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # j=0
        # ans=0
        # set1=set()
        # # for index,char in enumerate(s):
        # #     while char in set1:
        # #         set1.remove(s[j])
        # #         j+=1
        # #     set1.add(char)
        # #     ans=max(ans,index-j+1)
        # # return ans

        i=j=0
        ans=0
        set1=set()
        while i<len(s):
            if s[i] not in set1:
                set1.add(s[i])
                ans=max(ans,i-j+1)
                i+=1
            else:
                set1.remove(s[j])
                j+=1
        return ans