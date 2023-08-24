class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # pre = strs[0]
        # for i in strs:
        #     while not i.startswith(pre):
        #         pre = pre[:-1]
        # return pre   

        #sorting
        strs.sort()
        ans=""
        first=strs[0]
        last=strs[-1]
        for i in range(len(first)):
            if first[i]==last[i]:
                ans+=first[i]
            else:
                break
        return ans

        


        
