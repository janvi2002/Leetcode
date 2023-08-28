class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        for i in words:
#             here we keep two maps fo "ccc" type case so we make two way connection to recheck the pattern
            mp1={}
            mp2={}
            flag=1
#             pattern to word connection
            for j in range(len(i)):
                if pattern[j] not in mp1:
                    mp1[pattern[j]]=i[j]
                elif mp1[pattern[j]]!=i[j]:
                    flag=0
                    break
#             word to pattern connection for recheck condition
            for j in range(len(i)):
                if i[j] not in mp2:
                    mp2[i[j]]=pattern[j]
                elif mp2[i[j]]!=pattern[j]:
                    flag=0
                    break
            if flag:
                ans.append(i)
            
        return ans