class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map1=[]
        map2=[]
#         s="paper"
        for i in s:
            map1.append(s.index(i))
#      [0,1,0,3,4]  as index gives the first index value

#        t="title"
        for j in t:
            map2.append(t.index(j))
#      [0,1,0,3,4]

        if map1==map2:  #if they r equal means they easily swap each other fully
            return True
        return False
            
                
            