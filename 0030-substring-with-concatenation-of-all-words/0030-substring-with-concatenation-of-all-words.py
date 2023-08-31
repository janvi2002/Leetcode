class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         for making frequency of words
        map1={}
        for i in words:
            map1[i]=map1.get(i,0)+1
        
#         now we using sliding window inside sliding window
        i=0
        j=(len(words[0])*len(words))-1   #the size of main window is the length of wone word * length of array 
        ans=[]
        while j<len(s):
#       this is for inner window frequency 
            map2={}
            a=i
            b=i+len(words[0])-1   # size of inner window is len of word and we do i+ coz everytime we increase b with i value
#             here we add all inner window in hashmap
            while b<=j:
                map2[s[a:b+1]]=map2.get(s[a:b+1],0)+1
                
                a=b+1
                b+=len(words[0])
#             at last we check if both are equal in size then append starting index into the answer
            if map1==map2:
                ans.append(i)
            i+=1
            j+=1
        return ans
            
            