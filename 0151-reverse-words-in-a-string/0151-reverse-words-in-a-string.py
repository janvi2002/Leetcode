class Solution:
    def reverseWords(self, s: str) -> str:
        # ans=s.split()
        # ans.reverse()
        # return " ".join(ans)

        res=""
        i=0
        while i<len(s):
            while i<len(s) and s[i]==" ":   #first char after space
                i+=1
            if i>=len(s):
                break

            j=i+1

            while j<len(s) and s[j]!=" ":    #first char before space for a word
                j+=1
                
            if len(res)==0:    #for first word
                res=s[i:j]
            else:
                res=s[i:j]+" "+res   #for other word just add it before


            i=j+1
        return res



    

