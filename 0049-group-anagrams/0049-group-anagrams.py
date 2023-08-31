class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        dic={}
        for i in strs:
            temp="".join(sorted(i))
            if temp not in dic:
                dic[temp]=[i]
            else:
                dic[temp].append(i)
        for v in dic.values():
            ans.append(v)
        return ans