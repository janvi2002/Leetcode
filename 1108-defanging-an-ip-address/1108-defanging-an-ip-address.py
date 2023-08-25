class Solution:
    def defangIPaddr(self, adress: str) -> str:
        # adress=adress.replace(".","[.]")
        # return adress
        ans=""
        for  i in adress:
            if i==".":
                ans+="[.]"
            else:
                ans+=i
        return ans