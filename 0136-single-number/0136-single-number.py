class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dic={}
        # for i in nums:
        #     if i not in dic:
        #         dic[i]=1
        #     else:
        #         dic[i]+=1
        
        # for k,v in dic.items():
        #     if v==1:
        #         return k

        # by using xor

        xor=0
        for i in nums:
            xor=xor^i
        return xor
                